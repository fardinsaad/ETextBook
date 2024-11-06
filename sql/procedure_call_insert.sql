USE ETextBook;

-- Call the AddUser procedure to insert a new user: Admin
CALL AddUser('FaSa1106', 'Fardin','Saad','fsaad@ncsu.edu', 'FS!003$','Admin');

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