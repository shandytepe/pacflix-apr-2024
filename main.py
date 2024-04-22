from tabulate import tabulate

data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class User:
    
    def __init__(self, username: str):
        self.username = username
        
    # method check plan
    def check_benefit(self):
        """Method yang digunakan untuk menampilkan all benefits dari PacFlix"""
        # init headers
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Benefits"]
        
        # init data
        table = [[True, True, True, "Bisa Stream"],
                 [True, True, True, "Bisa Download"],
                 [True, True, True, "Kualitas SD"],
                 [False, True, True, "Kualitas HD"],
                 [False, False, True, "Kualitas UHD"],
                 [1, 2, 4, "Number of Devices"],
                 ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
                 [120_000, 160_000, 200_000, "Harga"]]
        
        print("====== PacFlix Plan List ======")
        print("")
        print(tabulate(table, headers, tablefmt="github"))
        
    # method check benefit based on input username
    def check_plan(self, username: str):
        """
        Method yang digunakan untuk mengambil data user PacFlix based on username
        
        Paramaters
        ----------
        username (str): input username
        """
        # iterate keys and values based on data
        for keys, values in data.items():
            
            # create branching to filter username
            if username == keys:
                
                # create variable to store the value
                get_current_plan = values[0]
                get_duration_plan = values[1]
                
                print(f"Username: {username}")
                print(f"Current Plan: {get_current_plan}")
                print(f"Duration Plan: {get_duration_plan}")

    # method upgrade plan based on username
    def upgrade_plan(self, username: str, upgrade_plan: str) -> float:
        """
        Method untuk upgrade subscription PacFlix
        
        Parameters
        ----------
        ...
        
        Returns
        -------
        ...
        """
        DISCOUNT = 0.05
        
        # iterate keys and values based on data
        for keys, values in data.items():
            
            try:
                # create branching to filter username
                if username == keys:

                    # create variable to store the value
                    get_current_plan = values[0]
                    get_duration_plan = values[1]

                    if upgrade_plan != get_duration_plan:
                        # filter duration plan to get a discount 5%
                        if get_duration_plan > 12:
                            # logic discount
                            if upgrade_plan == "Basic Plan":
                                total_price = 120_000 - (120_000 * DISCOUNT)
                                
                                return total_price
                            
                            elif upgrade_plan == "Standard Plan":
                                total_price = 160_000 - (160_000 * DISCOUNT)
                                
                                return total_price
                            
                            elif upgrade_plan == "Premium Plan":
                                total_price = 200_000 - (200_000 * DISCOUNT)
                                
                                return total_price
                            
                            else:
                                raise Exception("Unknown plan")
                                
                        else:
                            # branching if not discount
                            if upgrade_plan == "Basic Plan":
                                total_price = 120_000
                                
                                return total_price
                            
                            elif upgrade_plan == "Standard Plan":
                                total_price = 160_000
                                
                                return total_price
                            
                            elif upgrade_plan == "Premium Plan":
                                total_price = 200_000
                                
                                return total_price
                            
                            else:
                                raise Exception("Unknown plan")
                        
                    else:
                        raise Exception("Plan tidak boleh sama!")
                        
            except:
                raise Exception("Unknown process")

class NewUser:
    
    referral_code = []
    
    def __init__(self, username: str):
        self.username = username
        
    # method to extract referral code from dictionary
    def get_referral_code(self, data):
        """
        Method untuk extract Referral Code pada Dictionary data
        ...
        """
        # iterate to data
        for value in data.values():
            ref_code = value[2]
            
            # append to empty list
            self.referral_code.append(ref_code)
            
        return self.referral_code
        
    # method untuk new user pick plan
    def pick_plan(self, new_plan, referral_code):
        
        # initiate discount
        DISCOUNT = 0.04
        
        if referral_code in self.referral_code:
            # proses lanjut
            if new_plan == "Basic Plan":
                total_price = 120_000 - (120_000 * DISCOUNT)
                
                return total_price
            
            elif new_plan == "Standard Plan":
                total_price = 160_000 - (160_000 * DISCOUNT)
                
                return total_price
            
            elif new_plan == "Premium Plan":
                total_price = 200_000 - (200_000 * DISCOUNT)
                
                return total_price
            
            else:
                raise Exception("Unknown plan!")
            
        else:
            raise Exception("Referral Code tidak ada!!!")

user_1 = User(username = "Shandy")

print(user_1.check_benefit())

print(user_1.upgrade_plan(username = user_1.username,
                          upgrade_plan = "Premium Plan"))