USE mysql;
USE ETextBook;

DELIMITER $$

-- Procedure to insert into User table
CREATE PROCEDURE AddUser(
    IN p_userID VARCHAR(20),
    IN p_firstName VARCHAR(20),
    IN p_lastName VARCHAR(20),
    IN p_email VARCHAR(50),
    IN p_password VARCHAR(20),
    IN p_role TEXT
)
BEGIN
    INSERT INTO ETextBook.User (userID, firstName, lastName, email, password, role)
    VALUES (p_userID, p_firstName, p_lastName, p_email, p_password, p_role);
END$$

-- Procedure to insert into Admin table
CREATE PROCEDURE AddAdmin(
    IN p_AID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Admin (AID)
    VALUES (p_AID);
END$$

-- Procedure to insert into TA table
CREATE PROCEDURE AddTA(
    IN p_TAID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.TA (TAID)
    VALUES (p_TAID);
END$$

-- Procedure to insert into Faculty table
CREATE PROCEDURE AddFaculty(
    IN p_FID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Faculty (FID)
    VALUES (p_FID);
END$$

-- Procedure to insert into Student table
CREATE PROCEDURE AddStudent(
    IN p_SID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Student (SID)
    VALUES (p_SID);
END$$

-- Procedure to insert into ETbook table
CREATE PROCEDURE AddETbook(
    IN p_textBookID INT,
    IN p_title VARCHAR(255),
    IN p_userID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.ETbook (textBookID, title, userID)
    VALUES (p_textBookID, p_title, p_userID);
END$$

-- Procedure to insert into Chapter table
CREATE PROCEDURE AddChapter(
    IN p_chapterID VARCHAR(20),
    IN p_title VARCHAR(255),
    IN p_textBookID INT,
    IN p_userID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Chapter (chapterID, title, textBookID, userID)
    VALUES (p_chapterID, p_title, p_textBookID, p_userID);
END$$

-- Procedure to insert into Section table
CREATE PROCEDURE AddSection(
    IN p_sectionID VARCHAR(20),
    IN p_title VARCHAR(255),
    IN p_textBookID INT,
    IN p_chapterID VARCHAR(20),
    IN p_userID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Section (sectionID, title, textBookID, chapterID, userID)
    VALUES (p_sectionID, p_title, p_textBookID, p_chapterID, p_userID);
END$$

-- Procedure to insert into ContentBlock table
CREATE PROCEDURE AddContentBlock(
    IN p_blockID VARCHAR(20),
    IN p_blockType VARCHAR(255),
    IN p_content TEXT,
    IN p_textBookID INT,
    IN p_chapterID VARCHAR(20),
    IN p_sectionID VARCHAR(20),
    IN p_userID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.ContentBlock (blockID, blockType, content, textBookID, chapterID, sectionID, userID)
    VALUES (p_blockID, p_blockType, p_content, p_textBookID, p_chapterID, p_sectionID, p_userID);
END$$

-- Procedure to insert into Activity table
CREATE PROCEDURE AddActivity(
    IN p_activityID VARCHAR(20),
    IN p_textBookID INT,
    IN p_chapterID VARCHAR(20),
    IN p_sectionID VARCHAR(20),
    IN p_blockID VARCHAR(20),
    IN p_userID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Activity (activityID, textBookID, chapterID, sectionID, blockID, userID)
    VALUES (p_activityID, p_textBookID, p_chapterID, p_sectionID, p_blockID, p_userID);
END$$

-- Procedure to insert into Question table
CREATE PROCEDURE AddQuestion(
    IN p_questionID VARCHAR(20),
    IN p_textBookID INT,
    IN p_chapterID VARCHAR(20),
    IN p_sectionID VARCHAR(20),
    IN p_blockID VARCHAR(20),
    IN p_activityID VARCHAR(20),
    IN p_question TEXT,
    IN p_OP1 TEXT,
    IN p_OP1_EXP TEXT,
    IN p_OP1_Label TEXT,
    IN p_OP2 TEXT,
    IN p_OP2_EXP TEXT,
    IN p_OP2_Label TEXT,
    IN p_OP3 TEXT,
    IN p_OP3_EXP TEXT,
    IN p_OP3_Label TEXT,
    IN p_OP4 TEXT,
    IN p_OP4_EXP TEXT,
    IN p_OP4_Label TEXT,
    IN p_userID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.Question (questionID, textBookID, chapterID, sectionID, blockID, activityID, question, OP1, OP1_EXP, OP1_Label, OP2, OP2_EXP, OP2_Label, OP3, OP3_EXP, OP3_Label, OP4, OP4_EXP, OP4_Label, userID)
    VALUES (p_questionID, p_textBookID, p_chapterID, p_sectionID, p_blockID, p_activityID, p_question, p_OP1, p_OP1_EXP, p_OP1_Label, p_OP2, p_OP2_EXP, p_OP2_Label, p_OP3, p_OP3_EXP, p_OP3_Label, p_OP4, p_OP4_EXP, p_OP4_Label, p_userID);
END$$

-- Procedure to insert into Course table
CREATE PROCEDURE AddCourse(
    IN p_courseID VARCHAR(20),
    IN p_textBookID INT,
    IN p_title VARCHAR(255),
    IN p_userID VARCHAR(20),
    IN p_startDate DATE,
    IN p_endDate DATE,
    IN p_courseType TEXT
)
BEGIN
    INSERT INTO ETextBook.Course (courseID, textBookID, title, userID, startDate, endDate, courseType)
    VALUES (p_courseID, p_textBookID, p_title, p_userID, p_startDate, p_endDate, p_courseType);
END$$

-- Procedure to insert into ActiveCourse table
CREATE PROCEDURE AddActiveCourse(
    IN p_uToken CHAR(7),
    IN p_courseID VARCHAR(20),
    IN p_coursecapacity INT
)
BEGIN
    INSERT INTO ETextBook.ActiveCourse (uToken, courseID, coursecapacity)
    VALUES (p_uToken, p_courseID, p_coursecapacity);
END$$

-- Procedure to insert into ActiveEnrollment table
CREATE PROCEDURE AddActiveEnrollment(
    IN p_studentID VARCHAR(20),
    IN p_uToken CHAR(7),
    IN p_c_status VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.ActiveEnrollment (studentID, uToken, c_status)
    VALUES (p_studentID, p_uToken, p_c_status);
END$$

-- Procedure to insert into Notification table
CREATE PROCEDURE AddNotification(
    IN p_userID VARCHAR(20),
    IN p_n_message TEXT,
    IN p_isRead BOOLEAN
)
BEGIN
    INSERT INTO ETextBook.Notification (userID, n_message, isRead)
    VALUES (p_userID, p_n_message, p_isRead);
END$$

-- Procedure to insert into ActiveCourseTA table
CREATE PROCEDURE AddActiveCourseTA(
    IN p_uToken CHAR(7),
    IN p_TAID VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.ActiveCourseTA (uToken, TAID)
    VALUES (p_uToken, p_TAID);
END$$

-- Procedure to insert into content_user_activity table
CREATE PROCEDURE AddContentUserActivity(
    IN p_userID VARCHAR(20),
    IN p_courseID VARCHAR(20),
    IN p_textBookID INT,
    IN p_chapterID VARCHAR(20),
    IN p_sectionID VARCHAR(20),
    IN p_blockID VARCHAR(20),
    IN p_activityID VARCHAR(20),
    IN p_questionID VARCHAR(20),
    IN p_isHidden_chap VARCHAR(20),
    IN p_isHidden_sec VARCHAR(20),
    IN p_isHidden_block VARCHAR(20),
    IN p_isHidden_act VARCHAR(20),
    IN p_isHidden_ques VARCHAR(20)
)
BEGIN
    INSERT INTO ETextBook.content_user_activity (userID, courseID, textBookID, chapterID, sectionID, blockID, activityID, questionID, isHidden_chap, isHidden_sec, isHidden_block, isHidden_act, isHidden_ques)
    VALUES (p_userID, p_courseID, p_textBookID, p_chapterID, p_sectionID, p_blockID, p_activityID, p_questionID, p_isHidden_chap, p_isHidden_sec, p_isHidden_block, p_isHidden_act, p_isHidden_ques);
END$$

-- Procedure to insert into StudentActivity table
CREATE PROCEDURE AddStudentActivity(
    IN p_studentID VARCHAR(20),
    IN p_textBookID INT,
    IN p_uToken VARCHAR(7),
    IN p_chapterID VARCHAR(20),
    IN p_sectionID VARCHAR(20),
    IN p_blockID VARCHAR(20),
    IN p_activityID VARCHAR(20),
    IN p_questionID VARCHAR(20),
    IN p_score INT,
    IN p_time_stamp TIMESTAMP
)
BEGIN
    INSERT INTO ETextBook.StudentActivity (studentID, textBookID, uToken, chapterID, sectionID, blockID, activityID, questionID, score, time_stamp)
    VALUES (p_studentID, p_textBookID, p_uToken, p_chapterID, p_sectionID, p_blockID, p_activityID, p_questionID, p_score, p_time_stamp);
END$$

DELIMITER ;