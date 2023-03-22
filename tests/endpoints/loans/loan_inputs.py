LoanResponse = {
    "item": {
        "id": 1,
        "amount": "$10000.00",
        "interest_rate": "3.000%",
        "loan_term": 60,
        "owner": "shaneoh"
    }
}

MissingLoanResponse = {
    "detail": "Loan with this ID does not exist"
}

InvalidMonthResponse = {
    "detail": "Please eneter a month in the valid range for this loan term"
}

LoanSummaryResponse = {
    "Current balance": "$9690.24",
    "Principal paid": "$309.76",
    "Interest paid": "$49.61"
}

LoanWithMissingUser = {
    "amount": 100000,
    "interest_rate": 3,
    "loan_term": 360,
    "owner": "bob"
}

LoanWithMissingUserResponse = {
    "detail": "User with this ID does not exist"
}

LoanScheduleResponse = [
    {
        "Month": 1,
        "Remaining balance": "$9845.31",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 2,
        "Remaining balance": "$9690.24",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 3,
        "Remaining balance": "$9534.78",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 4,
        "Remaining balance": "$9378.93",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 5,
        "Remaining balance": "$9222.69",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 6,
        "Remaining balance": "$9066.06",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 7,
        "Remaining balance": "$8909.04",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 8,
        "Remaining balance": "$8751.62",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 9,
        "Remaining balance": "$8593.81",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 10,
        "Remaining balance": "$8435.61",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 11,
        "Remaining balance": "$8277.01",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 12,
        "Remaining balance": "$8118.02",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 13,
        "Remaining balance": "$7958.63",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 14,
        "Remaining balance": "$7798.84",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 15,
        "Remaining balance": "$7638.65",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 16,
        "Remaining balance": "$7478.06",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 17,
        "Remaining balance": "$7317.07",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 18,
        "Remaining balance": "$7155.67",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 19,
        "Remaining balance": "$6993.87",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 20,
        "Remaining balance": "$6831.67",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 21,
        "Remaining balance": "$6669.06",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 22,
        "Remaining balance": "$6506.05",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 23,
        "Remaining balance": "$6342.63",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 24,
        "Remaining balance": "$6178.80",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 25,
        "Remaining balance": "$6014.56",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 26,
        "Remaining balance": "$5849.91",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 27,
        "Remaining balance": "$5684.84",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 28,
        "Remaining balance": "$5519.37",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 29,
        "Remaining balance": "$5353.48",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 30,
        "Remaining balance": "$5187.18",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 31,
        "Remaining balance": "$5020.46",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 32,
        "Remaining balance": "$4853.32",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 33,
        "Remaining balance": "$4685.77",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 34,
        "Remaining balance": "$4517.80",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 35,
        "Remaining balance": "$4349.41",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 36,
        "Remaining balance": "$4180.59",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 37,
        "Remaining balance": "$4011.36",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 38,
        "Remaining balance": "$3841.70",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 39,
        "Remaining balance": "$3671.62",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 40,
        "Remaining balance": "$3501.11",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 41,
        "Remaining balance": "$3330.17",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 42,
        "Remaining balance": "$3158.81",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 43,
        "Remaining balance": "$2987.02",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 44,
        "Remaining balance": "$2814.80",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 45,
        "Remaining balance": "$2642.15",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 46,
        "Remaining balance": "$2469.07",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 47,
        "Remaining balance": "$2295.56",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 48,
        "Remaining balance": "$2121.61",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 49,
        "Remaining balance": "$1947.23",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 50,
        "Remaining balance": "$1772.41",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 51,
        "Remaining balance": "$1597.15",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 52,
        "Remaining balance": "$1421.46",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 53,
        "Remaining balance": "$1245.32",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 54,
        "Remaining balance": "$1068.75",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 55,
        "Remaining balance": "$891.74",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 56,
        "Remaining balance": "$714.28",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 57,
        "Remaining balance": "$536.38",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 58,
        "Remaining balance": "$358.03",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 59,
        "Remaining balance": "$179.24",
        "Monthly payment": "$179.69"
    },
    {
        "Month": 60,
        "Remaining balance": "$0.00",
        "Monthly payment": "$179.69"
    }
]