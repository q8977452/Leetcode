def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend/divisor >=2147483648:
            return(2147483647)
        return(int(dividend/divisor))