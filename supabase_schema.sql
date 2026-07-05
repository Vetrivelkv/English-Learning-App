-- Run this in your Supabase SQL Editor

-- Enable UUID extension if not already enabled
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Progress table
CREATE TABLE progress (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    topic_name TEXT NOT NULL,
    round_number INTEGER NOT NULL,
    passed BOOLEAN DEFAULT FALSE,
    attempts INTEGER DEFAULT 0,
    high_score INTEGER DEFAULT 0,
    last_attempted_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(user_id, topic_name, round_number)
);

-- Setup RLS (Row Level Security) - Optional but good practice. We'll leave it public for this simple auth.
ALTER TABLE users DISABLE ROW LEVEL SECURITY;
ALTER TABLE progress DISABLE ROW LEVEL SECURITY;
