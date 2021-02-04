class Sql:
    selectall = "SELECT * FROM users";
    selectid = "SELECT * FROM users WHERE u_id='%s'";
    selectnick = "SELECT * FROM users WHERE u_nick='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";