DROP DATABASE pixly;
CREATE DATABASE pixly;
\connect pixly;

CREATE TABLE images (
    id TEXT PRIMARY KEY,
    file_name TEXT NOT NULL,
    date TEXT,
    pixel_x_dimension INTEGER,
    pixel_y_dimension INTEGER,
    make TEXT,
    model TEXT,
    url TEXT
);

