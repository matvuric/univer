<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
  <?php
    $form = '<form action="index.php" method="POST" >
        E-mail: <input id="email" name="email" />
        <br>     <br>     
        Password <input id="pass" name="pass" type="password" /> <br> 
        <br> 
        Retype password <input id="pass_check" name="pass_check" type="password" />
        <br> 
        <input type="submit"></form>';
    
    if ($_SERVER['REQUEST_METHOD'] == 'GET') {
      echo $form;
    }
     
    # разобраться что нужно написать здесь, чтобы данные выводились только в случае отправки формы методом POST
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
      $email = $_POST['email'];
      $pass1 = $_POST['pass'];
      $pass2 = $_POST['pass_check'];

      if($pass1 == $pass2) {
        $pass_md5 = md5($pass1);
        $pass_sha1 = sha1($pass1);
        echo '<p>Hello World</p>';
        echo '<h1>' . date('r') . '</h1>';
        echo "<h2>Приветствую с почтой $email! </h2>";
        echo "<p>Пароль: $pass1 </p>";
        echo "<p>md5: $pass_md5 </p>";
        echo "<p>sha1: $pass_sha1 </p>";
      } else {
        echo "<p>Пароли не совпадают</p>";
      }
      
    }
    
?> 
  </body>
</html>
