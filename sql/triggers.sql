USE mysql;
USE ETextBook;

-- Trigger for inserting into role-specific tables after inserting into User table
DELIMITER $$

CREATE TRIGGER after_user_insert
AFTER INSERT ON ETextBook.User
FOR EACH ROW
BEGIN
    IF NEW.role = 'Admin' THEN
        INSERT INTO ETextBook.Admin (AID) VALUES (NEW.userID);
    ELSEIF NEW.role = 'TA' THEN
        INSERT INTO ETextBook.TA (TAID) VALUES (NEW.userID);
    ELSEIF NEW.role = 'Faculty' THEN
        INSERT INTO ETextBook.Faculty (FID) VALUES (NEW.userID);
    ELSEIF NEW.role = 'Student' THEN
        INSERT INTO ETextBook.Student (SID) VALUES (NEW.userID);
    END IF;
END$$

DELIMITER ;

-- Trigger for inserting into Activity table after inserting into ContentBlock table
DELIMITER $$

CREATE TRIGGER after_contentblock_insert
AFTER INSERT ON ETextBook.ContentBlock
FOR EACH ROW
BEGIN
    IF NEW.blockType = 'activity' THEN
        INSERT INTO ETextBook.Activity (
            activityID, textBookID, chapterID, sectionID, blockID, userID
        ) VALUES (
            NEW.content, NEW.textBookID, NEW.chapterID, NEW.sectionID, NEW.blockID, NEW.userID
        );
    END IF;
END$$

DELIMITER ;

-- Trigger to check if course capacity is full before approving a student for a course
DELIMITER $$

CREATE TRIGGER before_activeenrollment_update
BEFORE UPDATE ON ETextBook.ActiveEnrollment
FOR EACH ROW
BEGIN
    DECLARE course_capacity INT;
    DECLARE enrolled_students INT;

    -- Check if the c_status is being updated to 'Enrolled'
    IF NEW.c_status = 'Enrolled' THEN
        -- Get the course capacity
        SELECT coursecapacity INTO course_capacity
        FROM ETextBook.ActiveCourse
        WHERE uToken = NEW.uToken;

        -- Get the number of enrolled students
        SELECT COUNT(*) INTO enrolled_students
        FROM ETextBook.ActiveEnrollment
        WHERE uToken = NEW.uToken AND c_status = 'Enrolled';

        -- Check if the course is full
        IF enrolled_students >= course_capacity THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Course capacity reached. Cannot enroll more students.';
        END IF;
    END IF;
END$$

DELIMITER ;

-- Trigger to send notification when course capacity is reached
DELIMITER $$

CREATE TRIGGER after_activeenrollment_update
AFTER UPDATE ON ETextBook.ActiveEnrollment
FOR EACH ROW
BEGIN
    DECLARE course_capacity INT;
    DECLARE enrolled_students INT;

    -- Check if the c_status is being updated to 'Enrolled'
    IF NEW.c_status = 'Enrolled' THEN
        -- Get the course capacity
        SELECT coursecapacity INTO course_capacity
        FROM ETextBook.ActiveCourse
        WHERE uToken = NEW.uToken;

        -- Get the number of enrolled students
        SELECT COUNT(*) INTO enrolled_students
        FROM ETextBook.ActiveEnrollment
        WHERE uToken = NEW.uToken AND c_status = 'Enrolled';

        -- Check if the course is full
        IF enrolled_students >= course_capacity THEN
            -- Send notification to all pending students
            INSERT INTO ETextBook.Notification (userID, n_message)
            SELECT studentID, 'Course capacity is full. You can''t enroll anymore'
            FROM ETextBook.ActiveEnrollment
            WHERE uToken = NEW.uToken AND c_status = 'Pending';
        END IF;
    END IF;
END$$

DELIMITER ;


-- Trigger to delete notification when isRead is updated to TRUE
DELIMITER $$

CREATE TRIGGER after_notification_update
AFTER UPDATE ON ETextBook.Notification
FOR EACH ROW
BEGIN
    -- Check if the isRead column is updated to TRUE
    IF NEW.isRead = TRUE THEN
        DELETE FROM ETextBook.Notification
        WHERE notificationID = NEW.notificationID;
    END IF;
END$$

DELIMITER ;

-- Trigger for checking the enddate is greater than the startdate for a course if admin is updating the course table
DELIMITER $$

CREATE TRIGGER before_course_update
BEFORE UPDATE ON ETextBook.Course
FOR EACH ROW
BEGIN
    IF NEW.endDate < NEW.startDate THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'endDate cannot be before startDate';
    END IF;
END$$

DELIMITER ;