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
    SELECT cb.content
    FROM ETextBook.ContentBlock cb
    WHERE cb.chapterID = '02' AND cb.textBookID = 101
    ORDER BY cb.sectionID, cb.blockID;
END //

DELIMITER ;
CALL GetContentsOfChapter02()

-- 6. Contents of Chapter 02 of Textbook 101 in Proper Sequence
DELIMITER //

CREATE PROCEDURE GetContentsOfChapter02()
BEGIN
    SELECT cb.content
    FROM ETextBook.ContentBlock cb
    WHERE cb.chapterID = '02' AND cb.textBookID = 101
    ORDER BY cb.sectionID, cb.blockID;
END //

DELIMITER ;
