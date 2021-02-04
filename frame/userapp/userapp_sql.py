class Sql:
    userlist = "SELECT * FROM users";
    userlistone = "SELECT * FROM users WHERE id='%s'";
    userinsert = "INSERT INTO users VALUE ('%s','%s','%s','%s',%d)";
    userupdate = "UPDATE users SET u_nick = '%s', u_pwd = '%s', u_name = '%s', u_age = %d WHERE id='%s'"



