<?php

require_once 'student_client/config/config.php';
require_once 'student_client/services/StudentService.php';

$students = StudentService::getAllStudents();

require_once 'student_client/views/views1.php';