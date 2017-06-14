# Project name
Stephanos-Kung-Fu-Club(Information Management System)

# Business Logic
- This is a kind of information management system.
- It storing student info, students' parents info, course info, payment info, rank info, rank record and rank requirement info
- partly refresh the page to show differnet info.

Student
 - show basic infomation of student(name, stu_num,  gender, age, DOB , date of join schoole, mobile number, email and address)
 - show parents information for each student (by link)
 - show course information that each student applied (by link)
 - show the rank of each student (by link)
 - show the payment information of each student (by link)

Parents
 - show parents basic information(name, gender, age, DOB, Relation to student, mobile, email)
 - show their children info/student info (by link)

Course
 - show course basic information(level, start date, end date, week, time) 
 - show the information of student who applied this course (by link)
 
Payment
 - show payment basic infomation(num, date, amount of money)
 - show which kind of course that was brought (by link)
 - student who did this payment (by link)
 
Rank
 - show rank basic information(title, belt color)
 - show rank requirement of each rank (by link)
 
Rank record
 - the date that each student gained
 - information of each student who got rank (by link)
 - rank that specific student got (by link)

Rank Requirement
 - requirement content for ranks
 - show relative rank (by link)

# Models and their Relationships
- one2many
- many2many
- extra many2many

# Techniques
Django, Sqlite, Html, CSS, Bootstrap

# How to achieve
