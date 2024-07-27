import sys
import logging
from src.logger import logging

def error_message_details(error, error_detail: sys):
    # need filename, line number, string_error_message
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    string_error_message = str(error)
    result_error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, string_error_message)
    return result_error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        # our custom error message
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1/0 # raise a division by zero exception
    except Exception as e:
        logging.info("Error: Division by Zero")
        raise CustomException(e, sys)
        

