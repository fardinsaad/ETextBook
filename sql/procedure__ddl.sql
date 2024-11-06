USE mysql;
CREATE SCHEMA IF NOT EXISTS ETextBook;
USE ETextBook;

DELIMITER //

CREATE PROCEDURE CreateUserTable()
BEGIN
    CREATE TABLE IF NOT EXISTS User (
        userID VARCHAR(20) PRIMARY KEY,
        firstName VARCHAR(20),
        lastName VARCHAR(20),
        email VARCHAR(50),
        password VARCHAR(20),
        role TEXT CHECK (role IN ('Admin', 'TA', 'Faculty', 'Student')),
        account_creation_date DATETIME DEFAULT CURRENT_TIMESTAMP
    );
END //

CREATE PROCEDURE CreateAdminTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Admin(
        AID VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (AID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateTATable()
BEGIN
    CREATE TABLE IF NOT EXISTS TA(
        TAID VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (TAID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateFacultyTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Faculty(
        FID VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (FID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateStudentTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Student(
        SID VARCHAR(20) PRIMARY KEY,
        FOREIGN KEY (SID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateETbookTable()
BEGIN
    CREATE TABLE IF NOT EXISTS ETbook(
        textBookID INT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        userID VARCHAR(20) NOT NULL,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateChapterTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Chapter(
        chapterID VARCHAR(20), -- SHOULD BE CHAR(6)
        title VARCHAR(255) NOT NULL,
        textBookID INT,
        userID VARCHAR(20) NOT NULL,
        UNIQUE(title, textBookID),
        PRIMARY KEY (chapterID, textBookID),
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateSectionTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Section (
        sectionID VARCHAR(20),
        title VARCHAR(255) NOT NULL,
        textBookID INT,
        chapterID VARCHAR(20),
        userID VARCHAR(20) NOT NULL,
        UNIQUE(textBookID, chapterID, title),
        PRIMARY KEY (sectionID, chapterID, textBookID),
        FOREIGN KEY (chapterID, textBookID) REFERENCES Chapter(chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateContentBlockTable()
BEGIN
    CREATE TABLE IF NOT EXISTS ContentBlock (
        blockID VARCHAR(20),
        blockType VARCHAR(255) CHECK (blockType IN ('text', 'picture', 'activity')),
        content TEXT,
        textBookID INT,
        chapterID VARCHAR(20),
        sectionID VARCHAR(20),
        userID VARCHAR(20) NOT NULL,
        PRIMARY KEY (sectionID, chapterID, textBookID, blockID),
        FOREIGN KEY (sectionID, chapterID, textBookID) REFERENCES Section(sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (chapterID, textBookID) REFERENCES Chapter(chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateActivityTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Activity (
        activityID VARCHAR(20),
        textBookID INT,
        chapterID VARCHAR(20),
        sectionID VARCHAR(20),
        blockID VARCHAR(20),
        userID VARCHAR(20) NOT NULL,
        PRIMARY KEY (activityID, blockID, sectionID, chapterID, textBookID),
        FOREIGN KEY (sectionID, chapterID, textBookID, blockID) REFERENCES ContentBlock(sectionID, chapterID, textBookID, blockID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sectionID, chapterID, textBookID) REFERENCES Section(sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (chapterID, textBookID) REFERENCES Chapter(chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateQuestionTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Question(
        questionID VARCHAR(20),
        textBookID INT,
        chapterID VARCHAR(20),
        sectionID VARCHAR(20),
        blockID VARCHAR(20),
        activityID VARCHAR(20),
        question TEXT,
        OP1 TEXT,
        OP1_EXP TEXT,
        OP1_Label TEXT,
        OP2 TEXT,
        OP2_EXP TEXT,
        OP2_Label TEXT,
        OP3 TEXT,
        OP3_EXP TEXT,
        OP3_Label TEXT,
        OP4 TEXT,
        OP4_EXP TEXT,
        OP4_Label TEXT,
        userID VARCHAR(20) NOT NULL,
        PRIMARY KEY (questionID, activityID, blockID, sectionID, chapterID, textBookID),
        FOREIGN KEY (activityID, blockID, sectionID, chapterID, textBookID) REFERENCES Activity(activityID, blockID, sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sectionID, chapterID, textBookID, blockID) REFERENCES ContentBlock(sectionID, chapterID, textBookID, blockID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sectionID, chapterID, textBookID) REFERENCES Section(sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (chapterID, textBookID) REFERENCES Chapter(chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateCourseTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Course (
        courseID VARCHAR(20) PRIMARY KEY,
        textBookID INT NOT NULL,
        title VARCHAR(255) NOT NULL,
        userID VARCHAR(20) NOT NULL,  
        startDate DATE NOT NULL,
        endDate DATE NOT NULL,
        courseType TEXT CHECK (courseType IN ('Active', 'Evaluation')),
        CHECK (endDate >= startDate),
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateActiveCourseTable()
BEGIN
    CREATE TABLE IF NOT EXISTS ActiveCourse (
        uToken CHAR(7) PRIMARY KEY,
        courseID VARCHAR(20) NOT NULL,
        coursecapacity INT NOT NULL,  
        FOREIGN KEY (courseID) REFERENCES Course(courseID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateActiveEnrollmentTable()
BEGIN
    CREATE TABLE IF NOT EXISTS ActiveEnrollment (
        studentID VARCHAR(20),
        uToken CHAR(7),
        c_status VARCHAR(20) CHECK (c_status IN ('Enrolled', 'Pending')) NOT NULL,
        PRIMARY KEY (studentID, uToken),
        FOREIGN KEY (studentID) REFERENCES User(userID),
        FOREIGN KEY (uToken) REFERENCES ActiveCourse(uToken)
    );
END //

CREATE PROCEDURE CreateNotificationTable()
BEGIN
    CREATE TABLE IF NOT EXISTS Notification (
        notificationID INT AUTO_INCREMENT,
        userID VARCHAR(20) NOT NULL,
        n_message TEXT NOT NULL,
        isRead BOOLEAN DEFAULT FALSE,
        PRIMARY KEY (notificationID),
        FOREIGN KEY (userID) REFERENCES User(userID)
    );
END //

CREATE PROCEDURE CreateActiveCourseTATable()
BEGIN
    CREATE TABLE IF NOT EXISTS ActiveCourseTA (
        uToken CHAR(7),
        TAID VARCHAR(20),
        PRIMARY KEY (uToken, TAID),
        FOREIGN KEY (uToken) REFERENCES ActiveCourse(uToken),
        FOREIGN KEY (TAID) REFERENCES TA(TAID)
    );
END //

CREATE PROCEDURE CreateContentUserActivityTable()
BEGIN
    CREATE TABLE IF NOT EXISTS content_user_activity (
        userID VARCHAR(20),
        courseID VARCHAR(20),
        textBookID INT,
        chapterID VARCHAR(20),
        sectionID VARCHAR(20),
        blockID VARCHAR(20),
        activityID VARCHAR(20) DEFAULT 'NULL',
        questionID VARCHAR(20) DEFAULT 'NULL',
        isHidden_chap VARCHAR(20) CHECK (isHidden_chap IN ('yes', 'no')) DEFAULT 'no',
        isHidden_sec VARCHAR(20) CHECK (isHidden_sec IN ('yes', 'no')) DEFAULT 'no',
        isHidden_block VARCHAR(20) CHECK (isHidden_block IN ('yes', 'no')) DEFAULT 'no',
        isHidden_act VARCHAR(20) CHECK (isHidden_act IN ('yes', 'no')) DEFAULT 'no',
        isHidden_ques VARCHAR(20) CHECK (isHidden_ques IN ('yes', 'no')) DEFAULT 'no',
        PRIMARY KEY (userID, courseID, textBookID, chapterID, sectionID, blockID, activityID, questionID),
        FOREIGN KEY (courseID) REFERENCES Course(courseID),
        FOREIGN KEY (sectionID, chapterID, textBookID, blockID) REFERENCES ContentBlock(sectionID, chapterID, textBookID, blockID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sectionID, chapterID, textBookID) REFERENCES Section(sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (chapterID, textBookID) REFERENCES Chapter(chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

CREATE PROCEDURE CreateStudentActivityTable()
BEGIN
    CREATE TABLE IF NOT EXISTS StudentActivity (
        studentID VARCHAR(20),
        textBookID INT,
        uToken VARCHAR(7),
        chapterID VARCHAR(20),
        sectionID VARCHAR(20),
        blockID VARCHAR(20),
        activityID VARCHAR(20),
        questionID VARCHAR(20),
        score INT DEFAULT 0,
        time_stamp TIMESTAMP NOT NULL,
        PRIMARY KEY (studentID, uToken, chapterID, sectionID, blockID, activityID, questionID),
        FOREIGN KEY (studentID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (uToken) REFERENCES ActiveCourse(uToken) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (questionID, activityID, blockID, sectionID, chapterID, textBookID) REFERENCES Question(questionID, activityID, blockID, sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (activityID, blockID, sectionID, chapterID, textBookID) REFERENCES Activity(activityID, blockID, sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sectionID, chapterID, textBookID, blockID) REFERENCES ContentBlock(sectionID, chapterID, textBookID, blockID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (sectionID, chapterID, textBookID) REFERENCES Section(sectionID, chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (chapterID, textBookID) REFERENCES Chapter(chapterID, textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE
    );
END //

DELIMITER ;
