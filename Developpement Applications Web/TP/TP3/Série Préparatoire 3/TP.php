<!DOCTYPE html>
<html lang="en">
<head>
  
  <title>Document</title>
</head>
<body>
  
  <!-- <select name="ville">
  
  $villes = array("OUJDA", "NADOR", "BERKANE", "JERADA");

  foreach ($villes as $ville) {
      echo "<option value='$ville'>$ville</option>";
  }
   -->
   <!-- </select>
  <ul> -->
  <!-- 
        $villes = array("OUJDA", "NADOR", "BERKANE", "JERADA");

        foreach ($villes as $ville) {
            echo "<li><a href='#'>$ville</a></li>";
        }
        
  </ul> -->

  
</body>
</html>

<?php
  echo "EX1: <br>";
  echo "using while : <br>";
  $i=1;
  while($i<=10):
    echo $i." ";
    $i++;
  endwhile;
  echo "<br>using for : <br>";
  
  for($j =1;$j<=10;$j++){
    echo $j." ";
  }
  echo "<br> using a function : <br>";
  function number_1to10(){
    for($j =1;$j<=10;$j++){
      echo $j." ";
    }
  }
  number_1to10();
  echo "<br> passing an arg : <br>";
  function number_1ton($n){
    for($j =1;$j<=$n;$j++){
      echo $j." ";
    }
  }
  number_1ton(5);
  echo "<br><br><br> EX2 :<br>";
  $villes = array("OUJDA", "NADOR", "BERKANE", "JERADA");
  foreach ($villes as $ville) {
    echo "<input type='checkbox' name='ville' value='$ville'>$ville<br>";
  }
  echo "<br>";
  foreach ($villes as $ville) {
    echo "<input type='radio' name='ville' value='$ville'>$ville<br>";
  }
 ?>