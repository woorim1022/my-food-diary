class Sql:
    selectall = "SELECT * FROM users";
    selectone = "SELECT * FROM users WHERE u_id='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";