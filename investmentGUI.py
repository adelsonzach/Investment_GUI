'''
Chapter 9 example (Page 249 - 250)
Program: investmentGUI.py
3/17/2025

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run properly!

GUI-based version of the Investment program from Chapter 3
'''

from breezypythongui import EasyFrame

class InvestmentCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Investment Calculator 2.0", width=400, height=400, resizable=False)

        # Labels and input fields
        self.addLabel(text="Initial Amount", row=0, column=0)
        self.amount = self.addFloatField(value=0.0, row=0, column=1, precision=2)

        self.addLabel(text="Number of Years", row=1, column=0)
        self.period = self.addIntegerField(value=0, row=1, column=1)

        self.addLabel(text="Interest Rate (%)", row=2, column=0)
        self.rate = self.addFloatField(value=0.0, row=2, column=1, precision=2)

        # Compute button
        self.compute = self.addButton(text="Compute", row=3, column=0, columnspan=2, command=self.compute)

        # Output area
        self.outputArea = self.addTextArea(text="", row=4, column=0, columnspan=2, width=50, height=15)

    def compute(self):
        """Computes the investment report based on the inputs and outputs to the text area widget using tabular format."""
        # Obtain and validate the inputs
        startBalance = self.amount.getNumber()
        years = self.period.getNumber()
        rate = self.rate.getNumber() / 100

        if startBalance <= 0 or years <= 0 or rate <= 0:
            self.outputArea.setText("All inputs must be greater than zero!")
            return

        # Set the header for the table
        result = f"{'Year':<10}{'Starting Balance':<20}{'Interest':<15}{'Ending Balance':<20}\n"
        result += "-" * 65 + "\n"

        # Compute and append the results for each year
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += f"{year:<10}{startBalance:<20.2f}{interest:<15.2f}{endBalance:<20.2f}\n"
            startBalance = endBalance

        # Output the result to the text area
        self.outputArea.setText(result)

# Global definition of the main() function
def main():
    # Instantiate an object from the class into mainloop()
    InvestmentCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
    main()
#ZADE