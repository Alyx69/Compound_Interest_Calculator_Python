import tkinter as tk
from tkinter import ttk



class CompoundInterestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Compound Interest Calculator")
        self.root.geometry("500x600")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input fields
        ttk.Label(main_frame, text="Initial Deposit :").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.initial_deposit = ttk.Entry(main_frame)
        self.initial_deposit.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.initial_deposit.insert(0, "10000")
        
        ttk.Label(main_frame, text="Annual Interest Rate (%):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.interest = ttk.Entry(main_frame)
        self.interest.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        self.interest.insert(0, "5")
        
        ttk.Label(main_frame, text="Monthly Contribution :").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.contribution = ttk.Entry(main_frame)
        self.contribution.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        self.contribution.insert(0, "100")
        
        ttk.Label(main_frame, text="Time Period (months):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.time_period = ttk.Entry(main_frame)
        self.time_period.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        self.time_period.insert(0, "60")
        
        # Calculate button
        ttk.Button(main_frame, text="Calculate", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=20)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Results labels
        ttk.Label(results_frame, text="Initial Deposit Growth:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.deposit_growth = ttk.Label(results_frame, text="0.00")
        self.deposit_growth.grid(row=0, column=1, sticky=tk.E, pady=5)
        
        ttk.Label(results_frame, text="Total Contributions:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.total_contributions = ttk.Label(results_frame, text="0.00")
        self.total_contributions.grid(row=1, column=1, sticky=tk.E, pady=5)
        
        ttk.Label(results_frame, text="Interest Earned:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.interest_earned = ttk.Label(results_frame, text="0.00")
        self.interest_earned.grid(row=2, column=1, sticky=tk.E, pady=5)
        
        ttk.Label(results_frame, text="Final Amount:", font=("TkDefaultFont", 10, "bold")).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.final_amount = ttk.Label(results_frame, text="0.00", font=("TkDefaultFont", 10, "bold"))
        self.final_amount.grid(row=3, column=1, sticky=tk.E, pady=5)
        
        # Add some padding to all children of main_frame
        for child in main_frame.winfo_children():
            child.grid_configure(padx=5)
    
    def format_number(self, number):
        # Format number with commas and 2 decimal places
        return "{:,.2f}".format(number)
            
    def calculate(self):
        try:
            # Get values from inputs
            initial_deposit = float(self.initial_deposit.get())
            interest = float(self.interest.get()) / 100  # Convert percentage to decimal
            contribution = float(self.contribution.get())
            time_period_months = int(self.time_period.get())
            
            # Calculate monthly rate
            monthly_rate = interest / 12
            
            # Calculate initial deposit growth
            deposit_growth = initial_deposit * (1 + monthly_rate) ** time_period_months
            
            # Calculate contribution growth
            contribution_growth = contribution * (((1 + monthly_rate) ** time_period_months - 1) / monthly_rate)
            
            # Calculate total contributions (without interest)
            total_contributions = contribution * time_period_months
            
            # Calculate final amount
            final_amount = deposit_growth + contribution_growth
            
            # Calculate interest earned
            interest_earned = final_amount - initial_deposit - total_contributions
            
            # Update results labels with formatted numbers (commas and 2 decimal places)
            self.deposit_growth.config(text=self.format_number(deposit_growth))
            self.total_contributions.config(text=self.format_number(total_contributions))
            self.interest_earned.config(text=self.format_number(interest_earned))
            self.final_amount.config(text=self.format_number(final_amount))
            
        except ValueError:
            # Handle invalid input
            self.final_amount.config(text="Invalid input")
            self.deposit_growth.config(text="Error")
            self.total_contributions.config(text="Error")
            self.interest_earned.config(text="Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundInterestCalculator(root)
    root.mainloop()