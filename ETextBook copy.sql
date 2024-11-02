SET GLOBAL sql_mode = '';

CREATE TABLE ETextBook.User (
    userID VARCHAR(20) PRIMARY KEY,
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    email VARCHAR(50),
    password VARCHAR(20),
    role TEXT CHECK (role IN ('Admin', 'TA', 'Faculty', 'Student')),
    account_creation_date DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE ETextBook.Admin(
    AID VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY (AID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ETextBook.TA(
    TAID VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY (TAID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE ETextBook.Faculty(
    FID VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY (FID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE ETextBook.Student(
    SID VARCHAR(20) PRIMARY KEY,
    FOREIGN KEY (SID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- DONE
CREATE TABLE ETextBook.ETbook(
    textBookID INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    userID VARCHAR(20) NOT NULL
);

-- Done
CREATE TABLE ETextBook.Chapter(
    chapterID VARCHAR(20), -- SHOULD BE CHAR(6)
    -- primaryChapterNumber INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    -- secondaryChapterNumber INT,
    textBookID INT,
    userID VARCHAR(20) NOT NULL,
    UNIQUE(title, textBookID),
    PRIMARY KEY (chapterID, textBookID),
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- NOT DONE
CREATE TABLE ETextBook.ETbookChapter (
    textBookID INT,
    chapterID VARCHAR(20),
    PRIMARY KEY (textBookID, chapterID),
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Done
CREATE TABLE ETextBook.Section (
    sectionID VARCHAR(20),
    title VARCHAR(255) NOT NULL,
    -- primarySectionNumber VARCHAR(20) NOT NULL,
    -- secondarySectionNumber VARCHAR(20)
    chapterID VARCHAR(20),
    textBookID INT,
    userID VARCHAR(20) NOT NULL,
    UNIQUE(chapterID, title)
    PRIMARY KEY (sectionID, chapterID, textBookID)
);

-- NOT DONE
CREATE TABLE ETextBook.ChapterSection (
    chapterID VARCHAR(20),
    sectionID VARCHAR(20),
    PRIMARY KEY (chapterID, sectionID),
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- DONE
CREATE TABLE ETextBook.ContentBlock (
    blockID VARCHAR(20) PRIMARY KEY,
    blockType VARCHAR(255) CHECK (blockType IN ('text', 'picture', 'activity')),
    content TEXT
    sectionID VARCHAR(20),
    chapterID VARCHAR(20),
    textBookID INT,
    userID VARCHAR(20) NOT NULL,
    UNIQUE (sectionID, blockID)
    PRIMARY KEY (sectionID, chapterID, textBookID, blockID),
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
);

-- NOT DONE
CREATE TABLE ETextBook.SectionContentBlock (
    sectionID VARCHAR(20),
    blockID VARCHAR(20),
    PRIMARY KEY (sectionID, blockID),
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- CREATE TRIGGER ETextBook.Activity() insert after create content block
--DONE
CREATE TABLE ETextBook.Activity (
    activityID VARCHAR(20),
    blockID VARCHAR(20) PRIMARY KEY,
    sectionID VARCHAR(20),
    chapterID VARCHAR(20),
    textBookID INT,
    userID VARCHAR(20) NOT NULL,
    PRIMARY KEY (activityID, blockID, sectionID, chapterID, textBookID),
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE
);
-- DONE
CREATE TABLE ETextBook.Question(
    questionID VARCHAR(20),
    activityID VARCHAR(20),
    blockID VARCHAR(20) PRIMARY KEY,
    sectionID VARCHAR(20),
    chapterID VARCHAR(20),
    textBookID INT,
    OP1 TEXT,
    OP1_EXP TEXT,
    OP2 TEXT,
    OP2_EXP TEXT,
    OP3 TEXT,
    OP3_EXP TEXT,
    OP4 TEXT,
    OP4_EXP TEXT,
    CORRECT_OP INT,
    userID VARCHAR(20) NOT NULL,
    PRIMARY KEY (activityID, blockID, sectionID, chapterID, textBookID),
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- CREATE TRIGGER ETextBook.Question() insert after QUESTION

-- NOT DONE
CREATE TABLE ETextBook.ContentBlockActivity (
    blockID VARCHAR(20),
    activityID VARCHAR(20),
    PRIMARY KEY (blockID, activityID),
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (activityID) REFERENCES Activity(activityID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE ETextBook.EnrollmentWaitlist (
    UToken INT,
    studentID INT,
    PRIMARY KEY (UToken, studentID),
    FOREIGN KEY (UToken) REFERENCES Course(courseID),
    FOREIGN KEY (studentID) REFERENCES User(userID)
);

-- DONE
CREATE TABLE ETextBook.Course (
    courseID VARCHAR(20) PRIMARY KEY,
    textBookID INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    userID INT NOT NULL,  
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    courseType TEXT CHECK (courseType IN ('Active', 'Evaluation')), 
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- DONE
CREATE TABLE ETextBook.ActiveCourse (
    uToken CHAR(7) PRIMARY KEY,
    courseID VARCHAR(20) NOT NULL,
    coursecapacity INT NOT NULL,  
    FOREIGN KEY (courseID) REFERENCES Course(courseID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- DONE
CREATE TABLE ETextBook.ActiveEnrollment (
    studentID VARCHAR(20),
    uToken CHAR(7),
    c_status VARCHAR(20) CHECK (c_status IN ('Enrolled', 'Pending')) NOT NULL,
    PRIMARY KEY (studentID, uToken),
    FOREIGN KEY (studentID) REFERENCES User(userID),
    FOREIGN KEY (uToken) REFERENCES ActiveCourse(uToken)
);

-- DONE
CREATE TABLE ETextBook.Notification (
    notificationID INT,
    userID VARCHAR(20) NOT NULL,
    n_message TEXT NOT NULL,
    isRead BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (notificationID),
    FOREIGN KEY (userID) REFERENCES User(userID),
);

-- DONE
CREATE TABLE ETextBook.ActiveCourseTA (
    uToken CHAR(7),
    TAID VARCHAR(20),
    PRIMARY KEY (uToken, TAID),
    FOREIGN KEY (uToken) REFERENCES ActiveCourse(uToken),
    FOREIGN KEY (TAID) REFERENCES TA(TAID)
);

-- DONE
CREATE TABLE ETextBook.content_user_activity (
    userID VARCHAR(20),
    courseID VARCHAR(20),
    textBookID INT,
    chapterID VARCHAR(20),
    sectionID VARCHAR(20),
    blockID VARCHAR(20),
    activityID VARCHAR(20),
    questionID VARCHAR(20),
    isHidden_chap VARCHAR(20) CHECK (isHidden IN ('yes', 'no')) NOT NULL,
    isHidden_sec VARCHAR(20) CHECK (isHidden IN ('yes', 'no')) NOT NULL,
    isHidden_block VARCHAR(20) CHECK (isHidden IN ('yes', 'no')) NOT NULL,
    isHidden_act VARCHAR(20) CHECK (isHidden IN ('yes', 'no')) NOT NULL,
    isHidden_ques VARCHAR(20) CHECK (isHidden IN ('yes', 'no')) NOT NULL,
    PRIMARY KEY (userID, courseID, textBookID, chapterID, sectionID, blockID, activityID, questionID),
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (courseID) REFERENCES Course(courseID),
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID),
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID),
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID),
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID),
    FOREIGN KEY (activityID) REFERENCES Activity(activityID),
    FOREIGN KEY (questionID) REFERENCES Question(questionID)
)

-- maybe a procedure to update hidden status of content block


-- CREATE TABLE EvaluationCourse (
--     courseID INT PRIMARY KEY,
--     evaluationDate DATE,   
--     feedbackRequired BOOLEAN,     
--     FOREIGN KEY (courseID) REFERENCES Course(courseID) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- Done
CREATE TABLE ETextBook.StudentActivity (
    studentID VARCHAR(20),
    uToken VARCHAR(7),
    chapterID VARCHAR(20),
    sectionID VARCHAR(20),
    blockID VARCHAR(20),
    activityID VARCHAR(20),
    questionID VARCHAR(20),
    score INT DEFAULT 0,
    time_stamp TIMESTAMP NOT NULL,
    PRIMARY KEY (studentID, UToken, chapterID, sectionID, blockID, activityID, questionID),
    FOREIGN KEY (studentID) REFERENCES User(userID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (UToken) REFERENCES ActiveCourse(uToken) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (activityID) REFERENCES Activity(activityID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (questionID) REFERENCES Question(questionID) ON DELETE CASCADE ON UPDATE CASCADE
);





