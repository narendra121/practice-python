# try except fimnally
def causeError():
    try:
       return 1/0
    except Exception as e:
      return e
    finally:
        print("this will alway execute")
        
#catching by exception type

def causeError():
    try:
        return 1+'a'
    except TypeError:
        print("type error")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except Exception:
        print("some other")
        
#custom decorators

def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print("type error")
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except Exception:
            print("some other")
    return wrapper

@handleException
def causeError():
    return 1/0
causeError()

#raising exceptions
@handleException
def raiseError(n):
    if n==0:
      raise Exception()
    print(n)
    
#custom exception

class CustomException(Exception):
    pass

def causeError():
    raise CustomException("you called me")

causeError()



class HttpException(Exception):
    statusCode=None
    message=None
    def __init__(self):
        super().__init__(f"status code {self.statusCode} and status message{self.message}")
        
        
class NotFound(HttpException):
    statusCode=404
    message="resource not found"
def raiseNotfoundError():
    raise NotFound()

raiseNotfoundError()