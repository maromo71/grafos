class Conversor:
    @staticmethod
    def celsius_para_fahrenheit(celsius):
        return (celsius * 9/5.0) + 32

    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9.0
