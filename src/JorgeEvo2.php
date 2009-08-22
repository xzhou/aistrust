<?php
$VERBOSE=1;
$DEBUG=0;
$err=($argv[3]+0);
$delim = "\n";
$del1="alahay";
$del2="\n";
$set=($argv[1]);
$offset=($argv[2]+0);
$seed = 1180022396.99; //echo	(double)microtime(time); 5/24/07 12:00
//IO
//echo "<READING>\n";
$positive = "pre-pos.txt";
$fp = fopen($positive, "r");
$fpr = fread($fp, filesize($positive));

$aa = explode($delim, $fpr);
$ps = sizeof($aa);
$ii=0; $iii=0;
$ji=0;
for ($i=$offset; $i<$ps; $i++){	

//$bb = explode($del1, $aa[$i]);
//$cc = explode($del2, $bb[1]);
$cc[0] = $aa[$i];
$P[$i-$offset-1]= trim($cc[0]); //preg_replace("/[^a-z0-9-]/", " ", strip_tags(strtolower(trim($cc[0])))); 

}


unset($fpr);

$ji=0;
$positive = "pre-neg.txt";
$fp = fopen($positive, "r");
$fpr = fread($fp, filesize($positive));

$aa = explode($delim, $fpr);
$ps = sizeof($aa);
for ($i=$offset; $i<$ps; $i++){
//$bb = explode($del1, $aa[$i]);
//$cc = explode($del2, $bb[1]);
$cc[0] = $aa[$i];
$N[$i-$offset-1]= trim($cc[0]); //preg_replace("/[^a-z0-9-]/", " ", strip_tags(strtolower(trim($cc[0]))));

}
unset($fpr);


//$ftopw = fopen("topwords", "w");
//$ftopd = fopen("topdocs", "w");
//$ftf = fopen("wordyn.dat", "w");


//shuffle($P);
//shuffle($N);
/**************************************
************   INIT   *****************
**************************************/


$lag=0;
$Tr=200;
if ($err)
$Ts=2800;
else
$Ts=200;
$drE=0.1;
$drR=0.1;
$fr=0;
$APCS=6; //$argv[2];
$lopes=1;
$cKap = 9999; //$argv[3];
mt_srand($seed);
srand($seed);
$jj=(0);
$kk=0;
$jjj=($Tr);
$spamity=50;
for ($j=0; $j<$Tr; $j++){
$X[$j]=$P[$j];
$lnk[$j]=$j;
}
for ($j=$Tr; $j<($Tr+$Ts); $j++)
{
	if (mt_rand(0,100)>$spamity){
		$X[$j]=$P[$jjj];
		$fromz[$j]=$from[$jjj];
		$spam[$j]=0;
		$lnk[$j]=$jjj;
		$jjj++;
	}
	else{
		$X[$j]=$N[$jj];
		$spam[$j]=1;
		$jj++;
	}	

}

/*
//shuffle
for ($j=$Tr; $j<($Tr+$Ts); $j++){
$x = mt_rand($Tr,($Tr+$Ts-1));
$tspam = $spam[$j];
$tX = $X[$j];
$X[$j]=$X[$x];
$spam[$j]=$spam[$x];
$X[$x]=$tX;
$spam[$x]=$tspam;
}
*/
/*
//IDF
$bf = fopen("brownf.txt", "r");
$br = fread($bf, filesize("brownf.txt"));
$bx = explode("\n", $br);
for ($i=0; $i<sizeof($bx); $i++){
$tx = explode(" ", $bx[$i]);
$brow[strtolower($tx[0])]=$tx[1];
}
*/
/*
//RANDOM
if (mt_rand(0,100)>50)
$spam[$j]=1;
else
$spam[$j]=0;
*/
/*
//PARAMSEARCH
for ($APCS=2; $APCS<12; $APCGS+=2){ //apc
for ($cKap=40; $cKap<140; $cKap+=20){ //cKap
for ($l1=0.002; $l1<0.01; $l1+=0.002){ //dR
$drR=$l1;
$drE=$l1;
unset($sR);
unset($sE);
unset($R);
unset($E);
unset($A);
unset($Aw);
*/

//INIT
//echo "<TRAINING>\n";
for ($j=0; $j<sizeof($X); $j++){
$words = explode(" ", $X[$j]);



//entropy based
/*
if ($j>($Tr)){
unset($select);
for ($u=0; $u<sizeof($words); $u++){
if (isset($R[$words[$u]]))
$select[$words[$u]] = 0+abs($R[$words[$u]]-$E[$words[$u]]);
}


arsort($select);


$words = array_keys(array_slice($select, 0,50));
//shuffle($words);

}
else
{
*/

unset($bigrams);
unset($trigrams);
//bigrams
for ($u=1; $u<(sizeof($words)-2); $u++){
$bigrams[$u]=$words[$u]."--".$words[$u+1];
$trigrams[$u]=$words[$u]."--".$words[$u+1]."--".$words[$u+2];
}
//shuffle($words);
//shuffle($bigrams);
//shuffle($trigrams);
//$words = array_merge(array_slice($words, 2,52), array_slice($bigrams,2,52));
//$words = array_slice($words, 2,102);
//$words = array_slice($words, 2);

$words = array_merge(array_slice($trigrams, 2,152), array_merge(array_slice($words, 2,352), array_slice($bigrams,2,452)));





//IMMUNO DYNAMICS

$uwords = $words; //array_unique($words);


$cns[$j]=1;
foreach($uwords as $ta => $a){
if (strlen($a)>2){
	if (!isset($E[$a]) || !isset($R[$a] ) ){
		if ($j==1) $mwords[$a]=1;
		
		//$rwords[$a]=$j; //last occurance
		$E[$a]=6; //6
		if ($j<$Tr && $spam[$j]==0)
			$R[$a]=12; //12
		else 
			$R[$a]=5; //5

	}
	$T[$a]=$R[$a]+$E[$a];

}	
}

unset($Aw);
$Tdoc = 0;
foreach($uwords as $ta => $a){
	$A[$j]+=$APCS;
	$Aw[$a]+=$APCS;
	$Tdoc += $T[$a];
}


//$A[$j]=500;

unset($Lb);
unset($Ax);
$cn=0;
$Pr[$cn]=0;
$kk=0;
foreach($uwords	as $ta => $a){
	$R_[$a]=$R[$a];
	$E_[$a]=$E[$a];
	for ($jj=0; $jj<$Aw[$a]; $jj++){
		$T_[$a]=$R_[$a]+$E_[$a];
		if ($T_[$a]==0)
			$Ax[$kk]="_";
		else{
			$x = mt_rand(0,$T_[$a]);
			$Lb[$kk]=$a;		
			if ($x<$R_[$a]){
				$Ax[$kk]=1;
				if ($R_[$a]>0)
					$R_[$a]--;
			}

			else{
				$Ax[$kk]=0;
				if ($E_[$a]>0)
					$E_[$a]--;
			}
		}
		$kk++;
	}
}




$keys = array_keys($Ax);
shuffle($keys);

/*
for ($it=0; $it<(sizeof($keys)/2); $it++){
$tmmp = $keys[$it];
$ix = round(mt_rand(0,sizeof($keys)/2));
$keys[$it]=$keys[$ix];
$keys[$ix]=$tmmp;
}
for ($it=(sizeof($keys)/2); $it<(sizeof($keys)); $it++){
$tmmp = $keys[$it];
$ix = round(mt_rand(sizeof($keys)/2,sizeof($keys)));
$keys[$it]=$keys[$ix];
$keys[$ix]=$tmmp;
}
*/


$iii=0;
foreach ($keys as $key) {
  $Ax2[$iii] = $Ax[$key];
  $Lb2[$iii] = $Lb[$key];
$iii++;
}
$Ax = $Ax2;
$Lb = $Lb2;
//print_r($keys);
//print_r($Ax);
//print_r($Lb);

//$DEBUG=1;
//print_r($R);
//print_r($E);

for ($i=0; $i<$A[$j]; $i+=2){
	if ($Ax[$i]==="_" || $Ax[$i+1]==="_"){
if ($DEBUG) echo $i." ".$Ax[$i]." ".$Ax[$i+1]." ".($Ax[$i]+$Ax[$i+1])."\n";

	if ($Ax[$i+1]==0){
		if ($DEBUG) echo "_E ".$Lb[$i+1]."\n";
		if ($E[$Lb[$i+1]]<$cKap)
		$E[$Lb[$i+1]]++;
	}
	if ($Ax[$i]==0){
		if ($DEBUG) echo "E_ ".$Lb[$i]."\n";
		if ($E[$Lb[$i]]<$cKap)
		$E[$Lb[$i]]++;
	}
	}
	else{
		//CASE: A+E+E --> A+E+E+E+E	
		if (($Ax[$i]+$Ax[$i+1])==0 ){
		if ($E[$Lb[$i]]<$cKap)
			$E[$Lb[$i]]++;
		if ($E[$Lb[$i+1]]<$cKap)
			$E[$Lb[$i+1]]++;
		if ($DEBUG) echo "EE ".$Lb[$i]."/".$Lb[$i+1]."\n";
		}


		//CASE: A+E+R --> A+E+R+R	
		else if ((($Ax[$i])+($Ax[$i+1]))==1 ){
			if ($Ax[$i]==1){
		if ($R[$Lb[$i]]<$cKap)
				$R[$Lb[$i]]++;
		if ($DEBUG) echo "RE ".$Lb[$i]."/".$Lb[$i+1]."\n";
			}
			else{
		if ($R[$Lb[$i+1]]<$cKap)
				$R[$Lb[$i+1]]++;
		if ($DEBUG) echo "ER ".$Lb[$i]."/".$Lb[$i+1]."\n";
			}
		}

	}
}



//foreach($mwords as $a => $ta){
//if ($j==3){
//$kword[$a] = 1;
//}

//if ($j%15==1){
//fwrite($ftf, $j.".".$a."\t".$E[$a]."\t".$R[$a]."\n");
//fwrite($ftf, $j.".".$a."\t".($E[$a]/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\t".($R[$a]/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\n");
//fwrite($ftf, $j."\t".($E[$a]-$R[$a])."\n");

//if ($a=="more" ||  $a=="your" || $a=="you" || $a=="here" || $a=="free" || $a=="sex" || $a=="expect")

//if ($kword[$a]==1){
//if ($uwords[$a])
//fwrite($ftf, "(".$a.")\t".$j."\t".(($E[$a]-$R[$a])/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\n");
//else
//fwrite($ftf, $a."\t".$j."\t".(($E[$a]-$R[$a])/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\n");
//}
//}
//}


//	echo $j." ".sizeof($uwords)." ".sizeof($mwords)."\n";


foreach($mwords as $a => $ta){
if ($E[$a]>0)
$E[$a]=floor($E[$a]-($E[$a]*$drE));
if ($E[$a]>0)
$R[$a]=floor($R[$a]-($R[$a]*$drR));
}

/*
foreach($mwords as $a => $ta){

	$xE=0;
	for ($ii=0; $ii<$E[$a]; $ii++){
		$x = (mt_rand(0,1000)/1000);
		if ($x>=$drE)
			$xE++;
	}
	$E[$a]=$xE;
	$xR=0;
	for ($ii=0; $ii<$R[$a]; $ii++){
		$x = (mt_rand(0,1000)/1000);
		if ($x>=$drR)
			$xR++;
	}
	$R[$a]=$xR;

}
*/
unset($sw);
foreach($uwords as $ta => $a){
$sw[$a] = $E[$a]-$R[$a];
	if($E[$a]!=0 || $R[$a]!=0){
		$sE[$j] += (($E[$a]/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))/**(1-isset($brow[$a]))*/);
		$sR[$j] += (($R[$a]/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))/**(1-isset($brow[$a]))*/);
//if ($j%25==0){
//fwrite($ftf, $j.".".$a."\t".$E[$a]."\t".$R[$a]."\n");
//fwrite($ftf, $j.".".$a."\t".($E[$a]/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\t".($R[$a]/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\n");
//fwrite($ftf, $j."\t".($E[$a]-$R[$a])."\n");
//fwrite($ftf, $a."\t".$j."\t".(($E[$a]-$R[$a])/sqrt($E[$a]*$E[$a]+$R[$a]*$R[$a]))."\n");
//}

}
}

if ($VERBOSE){ 
echo $j."\t[".substr($X[$j],0,15)."]\t".round($sE[$j])."|".round($sR[$j])."\t";
for ($hi=0;$hi<$sE[$j]/5;$hi++)
	echo "E";
echo "/";
for ($hi=0;$hi<$sR[$j]/5;$hi++)
	echo "R"; 
echo "\n";
asort($sw);
$ki=0;
foreach ($sw as $aa => $a){
$ki++;
echo $a." ".$aa."\n";
if ($ki>3) break;
}
arsort($sw);
$ki=0;
foreach ($sw as $aa => $a){
$ki++;
echo $a." ".$aa."\n";
if ($ki>3) break;
}
}

unset($T);
}

$lab = array("Ham","Spam");

for ($i=$Tr; $i<($Ts+$Tr); $i++){


	$score[$i]=$sR[$i]-$sE[$i];
	$ss+=$score[$i];
	$ssn++;
}
if (!$err){
/*
echo "print(\"between ".$dateh[1]." and ".$dateh[1400]."\")\n";
echo "m<-rbind(";
for ($la=0; $la<=2400; $la+=10){
$lag=$la;
$_tp=0;
$_tn=0;
$_fp=0;
$_fn=0;
*/
$thresh=0; //$mean;
for ($i=($Tr+$lag); $i<($Tr+$lag+$Ts); $i++){



//for ($i=($Tr+$lag); $i<($Ts+$Tr); $i++){


		if ($spam[$i]==0){ 
//if (mt_rand(0,$spamity)<=30){
			$id = $i."".trim(substr(ereg_replace(" ",".",$X[$i]),0,20));
			//fwrite($fp, $id." ".($sE[$i]+0)." ".($sR[$i]+0)." P ".$score[$i]."\n");
			if ($score[$i]>$thresh)
				$_tp++;
			else
				$_fn++;
//		}
}
		else{
			$id = $i."".trim(substr(ereg_replace(" ",".",$X[$i]),0,20));
			//fwrite($fp, $id." ".($sE[$i]+0)." ".($sR[$i]+0)." N ".$score[$i]."\n");
			if ($score[$i]>$thresh)
				$_fp++;
			else
				$_tn++;
}
}

echo "\nTP ".$_tp."\n";
echo "FN ".$_fn."\n";
echo "TN ".$_tn."\n";
echo "FP ".$_fp."\n";
if (($_tp+$_fp)>0)
	echo "precision ".$_tp/($_tp+$_fp)."\n";
if (($_tp+$_fn)>0)
	echo "recall ".$_tp/($_tp+$_fn)."\n";
if (($_tn+$_fp)>0)
	echo "specificity ".$_tn/($_tn+$_fp)."\n";
if (($_tp+$_fn+$_fp+$_tn)>0)
	echo "accuracy ".($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn)."\n";

if (($_tp+$_fn)*($_tp+$_fp)>0)
{
	echo "F-score ".(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)))."\n";	
	//$ff[$A]=(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)));
}

//echo "c(".$_tp/($_tp+$_fp).",".$_tp/($_tp+$_fn).",".(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)))."),";

//echo "c(".($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn).",".(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp))).")";

/*
echo "c(".$_fn.",".$_fp.")";

if ($la<2400) echo ",";

}

echo ")\n";
echo '
m3 <- m;
for (i in 20:(length(m3[,1])-20)){m[i,1]<-mean(m3[(i-20):(i+20),1])}
for (i in 20:(length(m3[,2])-20)){m[i,2]<-mean(m3[(i-20):(i+20),2])}
plot(m[,1], type="n",ylim = c(0,50), main=paste("ICRM over enron", '.$set.'), xlab="slice", ylab="FP/FN"); text(m[,2], "FP", col="blue", cex=0.8); text(m[,1], "FN", col="red", cex=0.8);
abline(lsfit(1:length(m[,1]),m[,1]), col="red3", lwd="2"); abline(lsfit(1:length(m[,1]),m[,2]), col="blue3", lwd="2"); text(125,40, paste("slope coefficients = (",round(lsfit(1:length(m[,1]),m[,1])$coefficients[2],5),",", round(lsfit(1:length(m[,2]),m[,2])$coefficients[2],5),")"), font=2);
text(125, 45, paste("R-Squared = (",ls.print(lsfit(1:length(m[,1]),m[,1]), print.it=FALSE)$summary[2],",", ls.print(lsfit(1:length(m[,2]),m[,2]), print.it=FALSE)$summary[2],")"),font=2 );
hist(m3[,2], col="blue",angle=45,density=30, xlim=c(0,50), xlab="FP (blue) vs FN (red)",  main="FP/FN histogram"); hist(m3[,1],col="red",xlim=c(0,50),angle=-45,density=30, add=TRUE)
';
*/
/*
$totalscore[$APCS."-".$cKap."-".$drR]=(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)))*($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn); 
$totalscoreA[$APCS."-".$cKap."-".$drR]=($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn); 
$totalscoreF[$APCS."-".$cKap."-".$drR]=(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp))); 

}
}
}

arsort($totalscore);

foreach ($totalscore as $a => $as){
echo "[".$a."] F:".$totalscoreF[$a]."\tA:".$totalscoreA[$a]."\n";
}

*/
//}
}
else{
echo "print(\"between ".$dateh[1]." and ".$dateh[1400]."\")\n";
echo "m<-rbind(";
for ($la=0; $la<=2400; $la+=10){
$lag=$la;
$_tp=0;
$_tn=0;
$_fp=0;
$_fn=0;

$thresh=0; //$mean;
for ($i=($Tr+$lag); $i<($Tr+$lag+$Ts); $i++){



//for ($i=($Tr+$lag); $i<($Ts+$Tr); $i++){


                if ($spam[$i]==0){
//if (mt_rand(0,$spamity)<=30){
                        $id = $i."".trim(substr(ereg_replace(" ",".",$X[$i]),0,20));
                        //fwrite($fp, $id." ".($sE[$i]+0)." ".($sR[$i]+0)." P ".$score[$i]."\n");
                        if ($score[$i]>$thresh)
                                $_tp++;
                        else
                                $_fn++;
//              }
}
                else{
                        $id = $i."".trim(substr(ereg_replace(" ",".",$X[$i]),0,20));
                        //fwrite($fp, $id." ".($sE[$i]+0)." ".($sR[$i]+0)." N ".$score[$i]."\n");
                        if ($score[$i]>$thresh)
                                $_fp++;
                        else
                                $_tn++;
}
}

//echo "c(".$_tp/($_tp+$_fp).",".$_tp/($_tp+$_fn).",".(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)))."),";

//echo "c(".($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn).",".(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp))).")";


echo "c(".$_fn.",".$_fp.")";

if ($la<2400) echo ",";

}

echo ")\n";
echo '
mlim <- 0.25;
m <- m/200;
m3 <- m;
acc <- (400-m[,1]-m[,2])/400;
for (i in 20:(length(m3[,1])-20)){m[i,1]<-mean(m3[(i-20):(i+20),1])}
for (i in 20:(length(m3[,2])-20)){m[i,2]<-mean(m3[(i-20):(i+20),2])}
plot(m[,1], type="n",ylim = c(0,mlim), main=paste("ICRM over enron", '.$set.'), xlab="slice", ylab="%FP (black) %FN (red)"); text(m[,2], "FP", col="black", cex=0.8); text(m[,1], "FN", col="red", cex=0.8);
abline(lsfit(1:length(m[,1]),m[,1]), col="red3", lwd="2"); abline(lsfit(1:length(m[,2]),m[,2]), col="black", lwd="2");
text(125,0.8*mlim, col="blue", paste("slope coefficients = (",round(lsfit(1:length(m[,1]),m[,1])$coefficients[2],5),",", round(lsfit(1:length(m[,2]),m[,2])$coefficients[2],5),")"), font=2);
text(125, 0.9*mlim, col="blue", paste("R-Squared = (",ls.print(lsfit(1:length(m[,1]),m[,1]), print.it=FALSE)$summary[2],",", ls.print(lsfit(1:length(m[,2]),m[,2]), print.it=FALSE)$summary[2],")"),font=2 );
text(125,0.7*mlim, col="blue", paste("Average %FP=",round(mean(m[,2]),3), " %FN=",round(mean(m[,1]),3),  " %ERR=",round(mean(m),3)),  font=2);
#hist(m3[,2], col="black",angle=45,density=30, xlim=c(0,50), xlab="FP (black) vs FN (red)",  main="FP/FN histogram"); hist(m3[,1],col="red",xlim=c(0,50),angle=-45,density=30, add=TRUE)
';

/*
$totalscore[$APCS."-".$cKap."-".$drR]=(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)))*($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn);
$totalscoreA[$APCS."-".$cKap."-".$drR]=($_tp+$_tn)/($_tn+$_fp+$_tp+$_fn);
$totalscoreF[$APCS."-".$cKap."-".$drR]=(2*($_tp/($_tp+$_fp))*($_tp/($_tp+$_fn)))/(($_tp/($_tp+$_fn))+($_tp/($_tp+$_fp)));

}
}
}

arsort($totalscore);

foreach ($totalscore as $a => $as){
echo "[".$a."] F:".$totalscoreF[$a]."\tA:".$totalscoreA[$a]."\n";
}

//}
*/
}
