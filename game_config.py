class GAME:
    name = "Hra na život"
    screenplay = [
        "Tady je ta mapa {player}",
    ]
    input = {
        "Tady je ta mapa {player}": "self._map.print()",
    }

class PLAYER:
    name = "Nějkej ňouma"

class MAP:
    name = "Mapa"

ROOMS = [
    {
        "name": "Root",
        "direction": None,
        "data": {},
        "screenplay": [
            "Tak hele",
            "Jsou tady {rooms} dveře",
            "Viděl jsi mapu...",
            "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}"
        ],
        "input": {},
        "rooms": [
            {
                "name": "Javascript",
                "direction": "right",
                "data": {
                    "quiz": [
                        {
                            "question": "What is a correct syntax to output 'Hello World' in Python?",
                            "options": [
                                'p("Hello World")',
                                'print("Hello World")',
                                'echo "Hello World"'
                            ],
                            "answear": 1
                        },
                        {
                            "question": "How do you insert COMMENTS in Python code?",
                            "options": [
                                "/*This is a comment*/",
                                "//This is a comment",
                                "#This is a comment",
                            ],
                            "answear": 2
                        },
                        {
                            "question": 'Which one is NOT a legal variable name?',
                            "options": [
                                "my-var",
                                "Myvar",
                                "my_var"
                            ],
                            "answear": 0
                        },
                        {
                            "question": 'Which method can be used to remove any whitespace from both the beginning and the end of a string?',
                            "options": [
                                "trim()",
                                "len()",
                                "ptrim()",
                                "strip()"
                            ],
                            "answear": 3
                        },
                    ]
                },
                "screenplay": [
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}"
                ],
                "input": {
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}": "self.ask_questions(self.data['data']['quiz'])",
                },
            },
            {
                "name": "Python",
                "direction": "left",
                "data": {
                    "quiz": [
                        {
                            "question": "What is a correct syntax to output 'Hello World' in Python?",
                            "options": [
                                'p("Hello World")',
                                'print("Hello World")',
                                'echo "Hello World"'
                            ],
                            "answear": 1
                        },
                        {
                            "question": "How do you insert COMMENTS in Python code?",
                            "options": [
                                "/*This is a comment*/",
                                "//This is a comment",
                                "#This is a comment",
                            ],
                            "answear": 2
                        },
                        {
                            "question": 'Which one is NOT a legal variable name?',
                            "options": [
                                "my-var",
                                "Myvar",
                                "my_var"
                            ],
                            "answear": 0
                        },
                        {
                            "question": 'Which method can be used to remove any whitespace from both the beginning and the end of a string?',
                            "options": [
                                "trim()",
                                "len()",
                                "ptrim()",
                                "strip()"
                            ],
                            "answear": 3
                        },
                    ]
                },
                "screenplay": [
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}",
                ],
                "input": {
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}": "self.ask_questions(self.data['data']['quiz'])",
                }
            },
            {
                "name": "SQL",
                "direction": "straight",
                "data": {
                    "quiz": [
                        {
                            "question": 'With SQL, how do you select a column named "FirstName" from a table named "Persons"?',
                            "options": [
                                "SELECT FirstName FROM Persons",
                                "EXTRACT FirstName FROM Persons",
                                "SELECT Persons.FirstName"
                            ],
                            "answear": 0
                        },
                        {
                            "question": 'With SQL, how do you select all the records from a table named "Persons" where the value of the column "FirstName" is "Peter"?',
                            "options": [
                                "SELECT * FROM Persons WHERE FirstName='Peter'  ",
                                "SELECT [all] FROM Persons WHERE FirstName LIKE 'Peter'",
                                "SELECT [all] FROM Persons WHERE FirstName='Peter'"
                            ],
                            "answear": 0
                        },
                    ]
                },
                "screenplay": [
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}"
                ],
                "input": {
                    "Byl by jsi fakt ňouma, kdyby jsi něco pokazil {player}": "self.ask_questions(self.data['data']['quiz'])",
                },
            },
        ]
    },
]