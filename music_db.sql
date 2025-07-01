-- 음악 정보 테이블 생성
CREATE TABLE music (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    artist VARCHAR(100) NOT NULL,
    album VARCHAR(100) NOT NULL,
    release_year INT NOT NULL,
    genre VARCHAR(50) NOT NULL,
    duration INT NOT NULL, -- 초 단위
    likes INT NOT NULL DEFAULT 0
);

-- 예시 데이터 삽입
INSERT INTO music (title, artist, album, release_year, genre, duration, likes) VALUES
('Dynamite', 'BTS', 'BE', 2020, 'K-pop', 199, 1000000),
('Spring Day', 'BTS', 'You Never Walk Alone', 2017, 'K-pop', 255, 950000),
('How You Like That', 'BLACKPINK', 'THE ALBUM', 2020, 'K-pop', 182, 890000),
('Maria', 'Hwasa', 'Maria', 2020, 'K-pop', 195, 450000),
('Celebrity', 'IU', 'Celebrity', 2021, 'K-pop', 195, 780000); 