USE ETextBook;

-- Call the AddUser procedure to insert a new user: Admin
CALL AddUser('FaSa1106', 'Fardin','Saad','fsaad@ncsu.edu', 'FS!003$','Admin');
CALL AddUser('NaHa1106', 'Nazmul','Haque','mhaque4@ncsu.edu', 'NH!003$','Admin');
CALL AddUser('SaCe1106', 'Sanjana','Cheerla','scheerl@ncsu.edu', 'SC!003$','Admin');
CALL AddUser('RaMo1106', 'Rawshan','Mowri','rmowri@ncsu.edu', 'RM!003$','Admin');

-- Call the AddUser procedure to insert a new user: Faculty
CALL AddUser('KeOg1024', 'Kemafor', 'Ogan', 'kogan@ncsu.edu', 'Ko2024!rpc', 'Faculty');
CALL AddUser('JoDo1024', 'John', 'Doe', 'john.doe@example.com', 'Jd2024!abc', 'Faculty');
CALL AddUser('SaMi1024', 'Sarah', 'Miller', 'sarah.miller@domain.com', 'Sm#Secure2024', 'Faculty');
CALL AddUser('DaBr1024', 'David', 'Brown', 'david.b@webmail.com', 'DbPass123!', 'Faculty');
CALL AddUser('EmDa1024', 'Emily', 'Davis', 'emily.davis@email.com', 'Emily#2024!', 'Faculty');
CALL AddUser('MiWi1024', 'Michael', 'Wilson', 'michael.w@service.com', 'Mw987secure', 'Faculty');

-- Call the AddUser procedure to insert a new user: TA
CALL AddUser('JaWi1024', 'James', 'Williams', 'jwilliams@ncsu.edu', 'jwilliams@1234', 'TA');
CALL AddUser('LiAl0924', 'Lisa', 'Alberti', 'lalberti@ncsu.edu', 'lalberti&5678@', 'TA');
CALL AddUser('DaJo1024', 'David', 'Johnson', 'djohnson@ncsu.edu', 'djohnson%@1122', 'TA');
CALL AddUser('ElCl1024', 'Ellie', 'Clark', 'eclark@ncsu.edu', 'eclark^#3654', 'TA');
CALL AddUser('JeGi0924', 'Jeff', 'Gibson', 'jgibson@ncsu.edu', 'jgibson$#9877', 'TA');

-- Call the AddUser procedure to insert a new user: Student
CALL AddUser('ErPe1024', 'Eric', 'Perrig', 'ez356@example.mail', 'qwdmq', 'Student');
CALL AddUser('AlAr1024', 'Alice', 'Artho', 'aa23@edu.mail', 'omdsws', 'Student');
CALL AddUser('BoTe1024', 'Bob', 'Temple', 'bt163@template.mail', 'sak+=', 'Student');
CALL AddUser('LiGa1024', 'Lily', 'Gaddy', 'li123@example.edu', 'cnaos', 'Student');
CALL AddUser('ArMo1024', 'Aria', 'Morrow', 'am213@example.edu', 'jwocals', 'Student');
CALL AddUser('KeRh1014', 'Kellan', 'Rhodes', 'kr21@example.edu', 'camome', 'Student');
CALL AddUser('SiHa1024', 'Sienna', 'Hayes', 'sh13@example.edu', 'asdqm', 'Student');
CALL AddUser('FiWi1024', 'Finn', 'Wilder', 'fw23@example.edu', 'f13mas', 'Student');
CALL AddUser('LeMe1024', 'Leona', 'Mercer', 'lm56@example.edu', 'ca32', 'Student');

-- Call AddETbook procedure to insert new textbooks
CALL AddETbook(101, 'Database Management Systems', 'NaHa1106');
CALL AddETbook(102, 'Fundamentals of Software Engineering', 'NaHa1106');
CALL AddETbook(103, 'Fundamentals of Machine Learning', 'NaHa1106');

-- Call AddChapter procedure to insert new chapters
CALL AddChapter('chap01', 'Introduction to Database', 101, 'NaHa1106');
CALL AddChapter('chap02', 'The Relational Model', 101, 'NaHa1106');
CALL AddChapter('chap01', 'Introduction to Software Engineering', 102, 'NaHa1106');
CALL AddChapter('chap02', 'Introduction to Software Development Life Cycle (SDLC)', 102, 'NaHa1106');
CALL AddChapter('chap01', 'Introduction to Machine Learning', 103, 'NaHa1106');

-- Call AddSection procedure to insert new sections
CALL AddSection('Sec01', 'Database Management Systems (DBMS) Overview', 101, 'chap01', 'NaHa1106');
CALL AddSection('Sec02', 'Data Models and Schemas', 101, 'chap01', 'NaHa1106');
CALL AddSection('Sec01', 'Entities, Attributes, and Relationships', 101, 'chap02', 'NaHa1106');
CALL AddSection('Sec02', 'Normalization and Integrity Constraints', 101, 'chap02', 'NaHa1106');
CALL AddSection('Sec01', 'History and Evolution of Software Engineering', 102, 'chap01', 'NaHa1106');
CALL AddSection('Sec02', 'Key Principles of Software Engineering', 102, 'chap01', 'NaHa1106');
CALL AddSection('Sec01', 'Phases of the SDLC', 102, 'chap02', 'NaHa1106');
CALL AddSection('Sec02', 'Agile vs. Waterfall Models', 102, 'chap02', 'NaHa1106');
CALL AddSection('Sec01', 'Overview of Machine Learning', 103, 'chap01', 'NaHa1106');
CALL AddSection('Sec02', 'Supervised vs Unsupervised Learning', 103, 'chap01', 'NaHa1106');

-- Call AddContentBlock procedure to insert new content blocks
CALL AddContentBlock('Block01', 'text', 'A Database Management System (DBMS) is software that enables users to efficiently create, manage, and manipulate databases. It serves as an interface between the database and end users, ensuring data is stored securely, retrieved accurately, and maintained consistently. Key features of a DBMS include data organization, transaction management, and support for multiple users accessing data concurrently.', 101, 'chap01', 'Sec01', 'NaHa1106');
CALL AddContentBlock('Block01', 'activity', 'ACT0', 101, 'chap01', 'Sec02', 'NaHa1106');
CALL AddContentBlock('Block01', 'text', 'DBMS systems provide structured storage and ensure that data is accessible through queries using languages like SQL. They handle critical tasks such as maintaining data integrity, enforcing security protocols, and optimizing data retrieval, making them essential for both small-scale and enterprise-level applications. Examples of popular DBMS include MySQL, Oracle, and PostgreSQL.', 101, 'chap02', 'Sec01', 'NaHa1106');
CALL AddContentBlock('Block01', 'picture', 'sample.png', 101, 'chap02', 'Sec02', 'NaHa1106');
CALL AddContentBlock('Block01', 'text', 'The history of software engineering dates back to the 1960s, when the "software crisis" highlighted the need for structured approaches to software development due to rising complexity and project failures. Over time, methodologies such as Waterfall, Agile, and DevOps evolved, transforming software engineering into a disciplined, iterative process that emphasizes efficiency, collaboration, and adaptability.', 102, 'chap01', 'Sec01', 'NaHa1106');
CALL AddContentBlock('Block01', 'activity', 'ACT0', 102, 'chap01', 'Sec02', 'NaHa1106');
CALL AddContentBlock('Block01', 'text', 'The Software Development Life Cycle (SDLC) consists of key phases including requirements gathering, design, development, testing, deployment, and maintenance. Each phase plays a crucial role in ensuring that software is built systematically, with feedback and revisions incorporated at each step to deliver a high-quality product.', 102, 'chap02', 'Sec01', 'NaHa1106');
CALL AddContentBlock('Block01', 'picture', 'sample2.png', 102, 'chap02', 'Sec02', 'NaHa1106');
CALL AddContentBlock('Block01', 'text', 'Machine learning is a subset of artificial intelligence that enables systems to learn from data, identify patterns, and make decisions with minimal human intervention. By training algorithms on vast datasets, machine learning models can improve their accuracy over time, driving advancements in fields like healthcare, finance, and autonomous systems.', 103, 'chap01', 'Sec01', 'NaHa1106');
CALL AddContentBlock('Block01', 'activity', 'ACT0', 103, 'chap01', 'Sec02', 'NaHa1106');

-- Activity table is populated based on the blockType of the ContentBlock Table (no need to insert into activity table)

-- Call AddQuestion procedure to insert new questions
CALL AddQuestion('Q1', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'What does a DBMS provide?', 'Data storage only', 'DBMS provides more than just storage', 'Incorrect', 'Data storage and retrieval', 'DBMS manages both storing and retrieving data', 'Correct', 'Only security features', 'DBMS also handles other functions', 'Incorrect', 'Network management', 'DBMS does not manage network infrastructure', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q2', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Which of these is an example of a DBMS?', 'Microsoft Excel', 'Excel is a spreadsheet application', 'Incorrect', 'MySQL', 'MySQL is a popular DBMS', 'Correct', 'Google Chrome', 'Chrome is a web browser', 'Incorrect', 'Windows 10', 'Windows is an operating system', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q3', 101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'What type of data does a DBMS manage?', 'Structured data', 'DBMS primarily manages structured data', 'Correct', 'Unstructured multimedia', 'While some DBMS systems can handle it, its not core', 'Incorrect', 'Network traffic data', 'DBMS doesnt manage network data', 'Incorrect', 'Hardware usage statistics', 'DBMS does not handle hardware usage data', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q1', 102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'What was the "software crisis"?', 'A hardware shortage', 'The crisis was related to software development issues', 'Incorrect', 'Difficulty in software creation', 'The crisis was due to the complexity and unreliability of software', 'Correct', 'A network issue', 'It was not related to networking', 'Incorrect', 'Lack of storage devices', 'The crisis was not about physical storage limitations', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q2', 102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Which methodology was first introduced in software engineering?', 'Waterfall model', 'Waterfall was the first formal software development model', 'Correct', 'Agile methodology', 'Agile was introduced much later', 'Incorrect', 'DevOps', 'DevOps is a more recent development approach', 'Incorrect', 'Scrum', 'Scrum is a part of Agile, not the first methodology', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q3', 102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'What challenge did early software engineering face?', 'Lack of programming languages', 'Programming languages existed but were difficult to manage', 'Incorrect', 'Increasing complexity of software', 'Early engineers struggled with managing large, complex systems', 'Correct', 'Poor hardware development', 'The issue was primarily with software, not hardware', 'Incorrect', 'Internet connectivity issues', 'Internet connectivity was not a challenge in early software', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q1', 103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'What is the primary goal of supervised learning?', 'Predict outcomes', 'The goal is to learn a mapping from inputs to outputs for prediction.', 'Correct', 'Group similar data', 'This is more aligned with unsupervised learning.', 'Incorrect', 'Discover patterns', 'This is not the main goal of supervised learning.', 'Incorrect', 'Optimize cluster groups', 'This is not applicable to supervised learning.', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q2', 103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Which type of data is used in unsupervised learning?', 'Labeled data', 'Unsupervised learning uses unlabeled data.', 'Incorrect', 'Unlabeled data', 'It analyzes data without pre-existing labels.', 'Correct', 'Structured data', 'Unlabeled data can be structured or unstructured.', 'Incorrect', 'Time-series data', 'Unsupervised learning does not specifically focus on time-series.', 'Incorrect', 'NaHa1106');
CALL AddQuestion('Q3', 103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'In which scenario would you typically use supervised learning?', 'Customer segmentation', 'This is more relevant to unsupervised learning.', 'Incorrect', 'Fraud detection', 'Supervised learning is ideal for predicting fraud based on labeled examples.', 'Correct', 'Market basket analysis', 'This is generally done using unsupervised methods.', 'Incorrect', 'Anomaly detection', 'While applicable, it is less common than fraud detection in supervised learning.', 'Incorrect', 'NaHa1106');

-- Call AddCourse procedure to insert new courses
CALL AddCourse('NCSUOganCSC440F24', 101, 'CSC440 Database Systems', 'KeOg1024', '2024-08-15', '2024-12-15', 'Active');
CALL AddCourse('NCSUOganCSC540F24', 101, 'CSC540 Database Systems', 'KeOg1024', '2024-08-17', '2024-12-15', 'Active');
CALL AddCourse('NCSUSaraCSC326F24', 102, 'CSC326 Software Engineering', 'SaMi1024', '2024-08-23', '2024-10-23', 'Active');
CALL AddCourse('NCSUDoeCSC522F24', 103, 'CSC522 Fundamentals of Machine Learning', 'JoDo1024', '2025-08-25', '2025-12-18', 'Evaluation');
CALL AddCourse('NCSUSaraCSC326F25', 102, 'CSC326 Software Engineering', 'SaMi1024', '2025-08-27', '2025-12-19', 'Evaluation');

-- Call AddActiveCourse procedure to insert new active courses
CALL AddActiveCourse('XYJKLM', 'NCSUOganCSC440F24', 60);
CALL AddActiveCourse('STUKZT', 'NCSUOganCSC540F24', 50);
CALL AddActiveCourse('LRUFND', 'NCSUSaraCSC326F24', 100);

-- Call AddActiveCourseTA procedure to insert new active course TAs
CALL AddActiveCourseTA('XYJKLM', 'JaWi1024');
CALL AddActiveCourseTA('STUKZT', 'LiAl0924');
CALL AddActiveCourseTA('LRUFND', 'DaJo1024');

-- Call AddActiveEnrollment procedure to insert new enrollments
CALL AddActiveEnrollment('ErPe1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('ErPe1024', 'STUKZT', 'Enrolled');
CALL AddActiveEnrollment('AlAr1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('BoTe1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('LiGa1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('LiGa1024', 'STUKZT', 'Enrolled');
CALL AddActiveEnrollment('ArMo1024', 'STUKZT', 'Enrolled');
CALL AddActiveEnrollment('ArMo1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('SiHa1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('FiWi1024', 'LRUFND', 'Enrolled');
CALL AddActiveEnrollment('LeMe1024', 'XYJKLM', 'Enrolled');
CALL AddActiveEnrollment('FiWi1024', 'XYJKLM', 'Pending');
CALL AddActiveEnrollment('LeMe1024', 'STUKZT', 'Pending');
CALL AddActiveEnrollment('AlAr1024', 'STUKZT', 'Pending');
CALL AddActiveEnrollment('SiHa1024', 'STUKZT', 'Pending');
CALL AddActiveEnrollment('FiWi1024', 'STUKZT', 'Pending');


-- Call AddStudentActivity procedure to insert new student activities
CALL AddStudentActivity('ErPe1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 11:10:00');
CALL AddStudentActivity('ErPe1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 1, '2024-08-01 14:18:00');
CALL AddStudentActivity('ErPe1024', 101, 'STUKZT', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 1, '2024-08-02 19:06:00');
CALL AddStudentActivity('AlAr1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 13:24:00');
CALL AddStudentActivity('BoTe1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 0, '2024-08-01 09:24:00');
CALL AddStudentActivity('LiGa1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 07:45:00');
CALL AddStudentActivity('LiGa1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 3, '2024-08-01 12:30:00');
CALL AddStudentActivity('LiGa1024', 101, 'STUKZT', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 3, '2024-08-03 16:52:00');
CALL AddStudentActivity('ArMo1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 1, '2024-08-01 21:18:00');
CALL AddStudentActivity('ArMo1024', 101, 'XYJKLM', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 3, '2024-08-01 05:03:00');
CALL AddStudentActivity('FiWi1024', 102, 'LRUFND', 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 1, '2024-08-29 22:41:00');

-- Call AddContentUserActivity procedure to insert new content user activities
CALL AddContentUserActivity('SaMi1024', 'NCSUSaraCSC326F24', 102, 'chap02', 'Sec01', 'Block01', 'NULL', 'NULL', 'no', 'yes', 'yes', 'no', 'no');
CALL AddContentUserActivity('JoDo1024', 'NCSUDoeCSC522F24', 103, 'chap01', 'Sec01', 'Block01', 'NULL', 'NULL', 'no', 'yes', 'yes', 'no', 'no');


