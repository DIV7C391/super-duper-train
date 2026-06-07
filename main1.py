def safe_divide(numerator, denominator):
    try:
        # Tries to perform calculations that could fail
        num = float(numerator)
        den = float(denominator)
        result = num / den
    except ZeroDivisionError as e:
        # Catches division by zero
        print(f"Error caught: Cannot divide by zero. Details: {e}")
        result = None
    except ValueError as e:
        # Catches bad data types (e.g. trying to convert "abc" to a float)
        print(f"Error caught: Invalid numeric input. Details: {e}")
        result = None
    else:
        # Executes only if the try block succeeds without any errors
        print("Calculation completed successfully!")
    finally:
        # Always executes to close resources or log steps
        print("Execution of safe_divide completed.")
        
    return result

# --- Testing the implementation ---

safe_divide(10,2)

safe_divide(10, 0)

safe_divide(10, "apple")


