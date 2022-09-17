# CN331-AS2
## Assignment #2 - Create Django Web App

## **Group Member**
- ธรรมศาสตร์ ทองแกมแก้ว 6410685033
- ธนภัทร สาระธรรม 6410685140

## **Link**
- [Video How to use page](https://tuipied.sharepoint.com/:v:/s/Pond728/EdVG26hiNllNmShNvdREa68Bmr9n6YaMHjmvFqx36F16yA?e=7NiBMm)
- [GitHub repo url](https://github.com/cn331-6410685033/cn331-as2.git)

## **Web Details**
- Admin can create and edit Course. In Course, they can custom these following field. 
    - Course Code
    - Course Name
    - Yeat
    - Semester
    - Max Seat
    - Quota Available

- Users, (Students), can login and then they can see these following.
    - All Courses
    - My Courses
    - Available Courses

- Users, (Students), can enroll courses in "Course" page and withdraw enrolled courses in "My Courses" page.

## **Project Detail**
- Create Django Web App, Project's name: **"Quota"**
- There are 2 application in the Project.
    1. courses
    2. users

## How to use ***Student***

1. Login by fill in username and password.
![Login Page](./Capture/Login.png "Login Page")

2. Welcome Page.
![Home page](./Capture/Welcome.png "Home page")

3. Click "All Courses" to view all courses that have opened.
![All Course page](./Capture/All%20Courses.png "All Courses")

4. Click "Home" to return to Homepage (Welcome Page).
![Home page](./Capture/Welcome.png "Home page")

5. Click "My Courses" to view the courses that you have enrolled.
![My Courses page](./Capture/My%20Courses.png "My Courses")

6. Click "Available Courses" to view the courses that you haven't enrolled yet.
![Available Courses page](./Capture/Available%20Courses.png "Available Courses")

7. Click "Log out" in Homepage to logout.
![Logout Page](./Capture/Logout.png "Logout")

## How to use ***Admin***

### **Web page**
Admin is almost the same as student but Admin can see students that they have enrolled in each courses
![Admin View](./Capture/Admin.png "Admin View")

### **Django Admin**
1. Get into url /admin to go to django admin login page. Fill in username and password.<br>
Username and password has to create by use terminal.<br>
<br>
python3 manage.py createsuperuser<br>
<br>

![Admin Django Login](./Capture/DjangoAdminLogin.png "Admin Django Login")

2. Django Admin first page
![Admin Django View](./Capture/DjangoAdminView.png "Admin Django View")

3. Click "Courses" in Courses to view courses.
![Admin Django Courses](./Capture/Django%20Courses.png "Admin Django Courses")
    - Admin can create new course by click "ADD COURSE" in the top right side of page.
    - Admin can edit field in each course by clicking Course Code.

4. Admin can view Student by get into Users
![Admin Django Student](./Capture/DjangoStudent.png "Admin Django Student")
    - Admin can create new student by click "ADD USER" in the top right side of page.
    - Admin can edit field in each student by clicking Username.