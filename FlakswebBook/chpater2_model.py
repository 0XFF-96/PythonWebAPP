class Role(db.Model):

    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permisssions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')


class Permission():
    FOLLOW = 
    COMMENT = 
    WRITE_ARITICLES = 
    ..


class Role(db.Model):

    @staticmethod
    def insert_roles():
        roels = {
                'User':(Permisssion.FOLLOW | 
                        Permisssion.COMMENT |
                        Permission.WRITE_ARTICLES, True), 
                'Moderator' : (Permission.FOLLOW |
                    )
                'Administrator' (0xff, False)
                }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None :
                roel = Role(name=r)
            role.permissions = role[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

