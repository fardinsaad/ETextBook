-- 1. Number of Sections in the First Chapter of a Textbook
DELIMITER //

CREATE PROCEDURE GetNumberOfSectionsInFirstChapter()
BEGIN
    SELECT c.textBookID, COUNT(s.sectionID) AS number_of_sections_in_first_chapter
	FROM ETextBook.Chapter c
	JOIN ETextBook.Section s ON c.chapterID = s.chapterID AND c.textBookID = s.textBookID
	WHERE (c.textBookID, c.chapterID) IN (
		SELECT textBookID, MIN(chapterID)
		FROM ETextBook.Chapter
		GROUP BY textBookID
	)
	GROUP BY c.textBookID, c.chapterID;
END //

DELIMITER ;

CALL GetNumberOfSectionsInFirstChapter()

-- 2. Names of Faculty and TAs of All Courses with Their Roles
DELIMITER //
CREATE PROCEDURE GetFacultyAndTAsWithRoles()
BEGIN
    SELECT c.courseID, u.firstName, u.lastName, 'Faculty' AS role
	FROM ETextBook.Course c
	JOIN ETextBook.User u ON c.userID = u.userID
	JOIN ETextBook.Faculty f ON u.userID = f.FID

	UNION

	SELECT ac.courseID, u.firstName, u.lastName, 'TA' AS role
	FROM ETextBook.ActiveCourse ac
	JOIN ETextBook.ActiveCourseTA acta ON ac.uToken = acta.uToken
	JOIN ETextBook.User u ON acta.TAID = u.userID;
END //
DELIMITER ;
CALL GetFacultyAndTAsWithRoles()

-- 3. Active Course Details with Faculty and Total Number of Students
DELIMITER //

CREATE PROCEDURE GetActiveCourseDetails()
BEGIN
    SELECT ac.courseID, u.firstName, u.lastName, COUNT(ae.studentID) AS total_students
    FROM ETextBook.ActiveCourse ac
    JOIN ETextBook.Course c ON ac.courseID = c.courseID
    JOIN ETextBook.User u ON c.userID = u.userID
    LEFT JOIN ETextBook.ActiveEnrollment ae ON ac.uToken = ae.uToken AND ae.c_status = 'Enrolled'
    GROUP BY ac.courseID, u.firstName, u.lastName;
END //

DELIMITER ;
CALL GetActiveCourseDetails()

-- 4. Course with the Largest Waiting List
DELIMITER //

CREATE PROCEDURE GetCourseWithLargestWaitingList()
BEGIN
    SELECT 
		ac.courseID, 
		COUNT(*) AS total_waiting_list
	FROM 
		ETextBook.ActiveEnrollment ae
	JOIN 
		ETextBook.ActiveCourse ac ON ae.uToken = ac.uToken
	WHERE 
		ae.c_status = 'Pending'
	GROUP BY 
		ac.courseID
	ORDER BY 
		total_waiting_list DESC
	LIMIT 1;
END //

DELIMITER ;
CALL GetCourseWithLargestWaitingList()

-- 5. Contents of Chapter 02 of Textbook 101 in Proper Sequence
DELIMITER //

CREATE PROCEDURE GetContentsOfChapter02()
BEGIN
    SELECT 
    s.sectionID,
    s.title AS section_title,
    cb.blockID,
    cb.blockType,
    cb.content AS block_content,
    a.activityID,
    a.userID AS activity_userID,
    q.questionID,
    q.question,
    q.OP1,
    q.OP1_EXP,
    q.OP1_Label,
    q.OP2,
    q.OP2_EXP,
    q.OP2_Label,
    q.OP3,
    q.OP3_EXP,
    q.OP3_Label,
    q.OP4,
    q.OP4_EXP,
    q.OP4_Label
	FROM 
		ETextBook.Section s
	JOIN 
		ETextBook.ContentBlock cb ON s.sectionID = cb.sectionID AND s.chapterID = cb.chapterID AND s.textBookID = cb.textBookID
	LEFT JOIN 
		ETextBook.Activity a ON cb.blockID = a.blockID AND cb.sectionID = a.sectionID AND cb.chapterID = a.chapterID AND cb.textBookID = a.textBookID
	LEFT JOIN 
		ETextBook.Question q ON a.activityID = q.activityID AND a.blockID = q.blockID AND a.sectionID = q.sectionID AND a.chapterID = q.chapterID AND a.textBookID = q.textBookID
	WHERE 
		s.chapterID = 'chap02' AND s.textBookID = 101
	ORDER BY 
		s.sectionID, cb.blockID, a.activityID, q.questionID;
END //

DELIMITER ;
CALL GetContentsOfChapter02()

# 6. Incorrect Answers and Explanations for Q2 of Activity0 in Sec02 of Chap01 in Textbook 101
DELIMITER //

CREATE PROCEDURE GetIncorrectAnswersAndExplanations()
BEGIN
    SELECT q.OP1 AS 'Incorrect Answer', q.OP1_EXP AS 'Explanation'
    FROM ETextBook.Question q
    WHERE q.questionID = 'Q2' AND q.activityID = 'ACT0' AND q.sectionID = 'Sec02' AND q.chapterID = 'chap01' AND q.textBookID = 101
    AND q.OP1_Label != 'Correct'
    UNION
    SELECT q.OP2 AS 'Incorrect Answer', q.OP2_EXP AS 'Explanation'
    FROM ETextBook.Question q
    WHERE q.questionID = 'Q2' AND q.activityID = 'ACT0' AND q.sectionID = 'Sec02' AND q.chapterID = 'chap01' AND q.textBookID = 101
    AND q.OP2_Label != 'Correct'
    UNION
    SELECT q.OP3 AS 'Incorrect Answer', q.OP3_EXP AS 'Explanation'
    FROM ETextBook.Question q
    WHERE q.questionID = 'Q2' AND q.activityID = 'ACT0' AND q.sectionID = 'Sec02' AND q.chapterID = 'chap01' AND q.textBookID = 101
    AND q.OP3_Label != 'Correct'
    UNION
    SELECT q.OP4 AS 'Incorrect Answer', q.OP4_EXP AS 'Explanation'
    FROM ETextBook.Question q
    WHERE q.questionID = 'Q2' AND q.activityID = 'ACT0' AND q.sectionID = 'Sec02' AND q.chapterID = 'chap01' AND q.textBookID = 101
    AND q.OP4_Label != 'Correct';
END //

DELIMITER ;
CALL GetIncorrectAnswersAndExplanations()

# 7. Books in Active Status by One Instructor and Evaluation Status by Another Instructor
DELIMITER //

CREATE PROCEDURE GetBooksInDifferentStatuses()
BEGIN
    SELECT DISTINCT c1.textBookID
    FROM ETextBook.Course c1
    JOIN ETextBook.Course c2 ON c1.textBookID = c2.textBookID
    WHERE c1.courseType = 'Active' AND c2.courseType = 'Evaluation' AND c1.userID != c2.userID;
END //

DELIMITER ;
CALL GetBooksInDifferentStatuses()


