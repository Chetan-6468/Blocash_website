<?php

@include 'config.php';

if(isset($_POST['submit'])){

   $name = mysqli_real_escape_string($conn, $_POST['name']);
   $email = mysqli_real_escape_string($conn, $_POST['email']);
   $pass = md5($_POST['password']);
   $cpass = md5($_POST['cpassword']);
   $user_type = $_POST['user_type'];

   $select = " SELECT * FROM user_form WHERE email = '$email' && password = '$pass' ";

   $result = mysqli_query($conn, $select);

   if(mysqli_num_rows($result) > 0){

      $error[] = 'user already exist!';

   }else{

      if($pass != $cpass){
         $error[] = 'password not matched!';
      }else{
         $insert = "INSERT INTO user_form(name, email, password, user_type) VALUES('$name','$email','$pass','$user_type')";
         mysqli_query($conn, $insert);
         header('location:login_form.php');
      }
   }

};


?>

<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>register form</title>

   <!-- custom css file link  -->
   <link rel="stylesheet" href="register.css">
   <link rel="shortcut icon" href="logos.jpg.png">

</head>
<body>
   
<div class="form-container">

   <form action="" method="post">
   <a href="/"><img src="logos.jpg.png" alt="blocash" height="50px" width="50px" />
								</a>
      <h3><b>Blocash</b></h3>
      <?php
      if(isset($error)){
         foreach($error as $error){
            echo '<span class="error-msg">'.$error.'</span>';
         };
      };
      ?>
      <input type="text" name="name" required placeholder="enter your name">
      <input type="email" name="email" required placeholder="enter your email">
      <input type="password" name="password" required placeholder="enter your password">
      <input type="password" name="cpassword" required placeholder="confirm your password">
      <select name="user_type">
         <option value="user">user</option>
         <option value="admin">admin</option>
      </select>
      <div class="field phone">

         <input type="text" name="phone" required placeholder="Phone Number" required id="id_phone" maxlength="13" />
         </div>
         
         <div class="field state">
         

         <select name="state" required id="id_state">
            <option value="" selected >State of residence</option>
         
            <option value="1">ANDAMAN AND NICOBAR ISLANDS</option>
         
            <option value="2">ANDHRA PRADESH</option>
         
            <option value="3">ARUNACHAL PRADESH</option>
         
            <option value="4">ASSAM</option>
         
            <option value="5">BIHAR</option>
         
            <option value="6">CHANDIGARH</option>
         
            <option value="7">DADRA &amp; NAGAR HAVELI</option>
         
            <option value="8">DAMAN &amp; DIU</option>
         
            <option value="9">DELHI</option>
         
            <option value="10">GOA</option>
         
            <option value="11">GUJARAT</option>
         
            <option value="12">HARYANA</option>
         
            <option value="13">HIMACHAL PRADESH</option>
         
            <option value="14">JAMMU AND KASHMIR</option>
         
            <option value="15">KARNATAKA</option>
         
            <option value="16">KERALA</option>
         
            <option value="17">LAKHSWADEEP</option>
         
            <option value="18">MADHYA PRADESH</option>
         
            <option value="19">MAHARASHTRA</option>
         
            <option value="20">MANIPUR</option>
         
            <option value="21">MEGHALAYA</option>
         
            <option value="22">MIZORAM</option>
         
            <option value="23">NAGALAND</option>
         
            <option value="24">ORISSA</option>
         
            <option value="25">PONDICHERRY</option>
         
            <option value="26">PUNJAB</option>
         
            <option value="27">RAJASTHAN</option>
         
            <option value="28">SIKKIM</option>
         
            <option value="29">TAMIL NADU</option>
         
            <option value="30">TRIPURA</option>
         
            <option value="31">UTTAR PRADESH</option>
         
            <option value="32">WEST BENGAL</option>
         
            <option value="33">CHHATTISGARH</option>
         
            <option value="34">UTTARKHAND</option>
         
            <option value="35">JHARKHAND</option>
         
            <option value="36">UNION TERRITORY</option>
         
            <option value="37">TELANGANA</option>
         
            <option value="98">APO</option>
         
         </select>
         </div>

         <div class="field disclaimer" style="font-family: 'Times New Roman', Times, serif;">
  
      <li >I understand the risks involved in trading stock, commodity, and currency
         markets.</li>
      <li>I understand the risks of my program not working as intended. I take full
         responsibility for any losses that may arise while trading programmatically.
      </li>
      <li>I have read the <a target='_blank' href='terms&condition.html'>Terms and
            Conditions</a> and accept it.</li>
         </label>
      I AGREE TO THE ABOVE TERMS:
<input type="checkbox" name="disclaimer" required id="id_disclaimer" />
</div>

      <input type="submit" name="submit" value="register now" class="form-btn">
      <p>already have an account? <a href="login_form.php">login now</a></p>




   </form>

</div>

</body>
</html>