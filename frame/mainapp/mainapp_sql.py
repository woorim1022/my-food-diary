class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE id='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";