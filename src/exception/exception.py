import sys

class CustomException(Exception):
    """
    To get more information about the exeption that occured.
    """
    def __init__(self, error_message, error_details:sys):

        self.error_message = error_message
        _,_,execution_traceback = error_details.exc_info()
        #Traceback object is created using execution_traceback

        self.line_no = execution_traceback.tb_lineno
        self.file_name = execution_traceback.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in python script file name: {self.file_name} in line no {self.line_no} with the following error: {self.error_message}"

if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        # raise e   #ZeroDivisionError: division by zero
        # print(e)  #divide by zero
        raise CustomException(e, sys)

