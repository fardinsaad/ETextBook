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

CREATE TABLE ETextBook.ETbook(
    textBookID INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);


CREATE TABLE ETextBook.Chapter(
    chapterID VARCHAR(20),
    primaryChapterNumber INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    secondaryChapterNumber INT,
    PRIMARY KEY (chapterID, primaryChapterNumber, title),
    UNIQUE(primaryChapterNumber, title, secondaryChapterNumber)
);


CREATE TABLE ETextBook.ETbookChapter (
    textBookID INT,
    chapterID VARCHAR(20),
    PRIMARY KEY (textBookID, chapterID),
    FOREIGN KEY (textBookID) REFERENCES ETbook(textBookID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE ETextBook.Section (
    sectionID VARCHAR(20),
    title VARCHAR(255) NOT NULL,
    primarySectionNumber VARCHAR(20) NOT NULL,
    secondarySectionNumber VARCHAR(20)
    PRIMARY KEY (sectionID, title),
);


CREATE TABLE ETextBook.ChapterSection (
    chapterID VARCHAR(20),
    sectionID VARCHAR(20),
    PRIMARY KEY (chapterID, sectionID),
    FOREIGN KEY (chapterID) REFERENCES Chapter(chapterID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE ETextBook.ContentBlock (
    blockID VARCHAR(20) PRIMARY KEY,
    blockType VARCHAR(255),
    content TEXT
);


CREATE TABLE ETextBook.SectionContentBlock (
    sectionID VARCHAR(20),
    blockID VARCHAR(20),
    PRIMARY KEY (sectionID, blockID),
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE ETextBook.Activity (
    activityID VARCHAR(20) PRIMARY KEY,
    sectionID VARCHAR(20),
    question TEXT,
    correctAnswer TEXT,
    inCorrectAnswer1 TEXT,
    inCorrectAnswer2 TEXT,
    inCorrectAnswer3 TEXT,
    explanation TEXT,
    FOREIGN KEY (sectionID) REFERENCES Section(sectionID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE ETextBook.ContentBlockActivity (
    blockID VARCHAR(20),
    activityID VARCHAR(20),
    PRIMARY KEY (blockID, activityID),
    FOREIGN KEY (blockID) REFERENCES ContentBlock(blockID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (activityID) REFERENCES Activity(activityID) ON DELETE CASCADE ON UPDATE CASCADE
);
