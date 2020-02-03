<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Not Buzzfeed Quiz</title>
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/all.css') }}">
  </head>
  <body>
    <div class="navbar">
      <i class="nav-icon fas fa-bars"></i>
      <a class="buzzfeed" href="#home">Not Buzzfeed</a>
      <ul>
        <li><a href="#news">News</a></li>
        <li><a href="#contact">Quizzes</a></li>
        <li><a href="#about">Shopping</a></li>
        <li><a href="#about">TV & Movies</a></li>
        <li><a href="#about">Videos</a></li>
      </ul>
      <i class="nav-icon fas fa-search"></i>
    </div>
    <br>
    <div class="row" style="width:100%">
      <img style="height:45px;float:left;padding-top:3px;" src="{{ url_for('static', filename='images/buzzfeedarrow.png') }}">
      <div style="width:100px;float:left;padding-left: 20px;padding-top:7px;">
        <div style="color:#757575;font-weight:400">TRENDING</div>
        <div style="color:#e32e32">172 Views</div>
      </div>
    <br><br><br>
    <h1>{{ heading }}</h1>
    {% for choice in choices %}
      <a href={{choice[1]}}>{{ choice[0] }}</a>
    {% endfor  %}
  </body>
</html>