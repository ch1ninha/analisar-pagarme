users = [{"user_1": {
            "id": "1010",
            "name":"Eli Manning",
            "email":"eli_manning@gmail.com",
            "cpf":"00179553003",
            "phone":"+5511999991010",
            "dob":"1980-10-10"
            }
         },
         {"user_2": {
            "id": "2727",
            "name":"Brandon Jacobs",
            "email":"brandon_giants@gmail.com",
            "cpf":"89473588003",
            "phone":"+5511999992828",
            "dob":"1975-01-01"
            }
        },
        {"user_3": {
            "id": "1717",
            "name":"Plaxico Burress",
            "email":"plaxico_shooter@gmail.com",
            "cpf":"09933610058",
            "phone":"+5511999991717",
            "dob":"1978-01-01"
            }
        },
        {"user_4": {
            "id": "9191",
            "name":"Justin Tuck",
            "email":"justinthegoat@gmail.com",
            "cpf":"68803517006",
            "phone":"+5511999999191",
            "dob":"1974-01-01"
            }
        }
    ]


class user:
    def __init__(self):
        self.users = [  {"user_1": {
                            "id": "1010",
                            "name":"Eli Manning",
                            "email":"eli_manning@gmail.com",
                            "cpf":"00179553003",
                            "phone":"+5511999991010",
                            "dob":"1980-10-10"
                            }
                        },
                        {"user_2": {
                            "id": "2727",
                            "name":"Brandon Jacobs",
                            "email":"brandon_giants@gmail.com",
                            "cpf":"89473588003",
                            "phone":"+5511999992828",
                            "dob":"1975-01-01"
                            }
                        },
                        {"user_3": {
                            "id": "1717",
                            "name":"Plaxico Burress",
                            "email":"plaxico_shooter@gmail.com",
                            "cpf":"09933610058",
                            "phone":"+5511999991717",
                            "dob":"1978-01-01"
                            }
                        },
                        {"user_4": {
                            "id": "9191",
                            "name":"Justin Tuck",
                            "email":"justinthegoat@gmail.com",
                            "cpf":"68803517006",
                            "phone":"+5511999999191",
                            "dob":"1974-01-01"
                            }
                        }
                     ]

    def get_user(self):
        global user_now
        user_now = self.users.pop()
        user_parm = {
            "customer": {
                "external_id": f"{user_now.get('id')}",
                "name": f"{user_now.get('name')}",
                "type": "individual",
                "country": "br",
                "email": f"{user_now.get('email')}",
                "documents": [
                    {
                    "type": "cpf",
                    "number": f"{user_now.get('cpf')}"
                    }
                ],
                "phone_numbers": [f"{user_now.get('phone')}"],
                "birthday": f"{user_now.get('dob')}"
            }
        }
        return user_parm

teste = user()

#print(teste.users)

teste.get_user()
print(user_now.keys())
print(user_now.get(user_now.keys())['id'])
