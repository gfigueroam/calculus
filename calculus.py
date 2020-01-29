def get_coefs_exps(poly):
   """Returns coefs and exps from a polynomial"""
   coefs= poly[0]  #coefficients of the polynomial terms
   exps = poly[1]  #exponentials of the polynomial terms
   return coefs,exps

def construct_poly(coefs,exps):
    """Return an poly object as a list of coefficients and exponents"""
    poly = []
    poly.append(coefs)
    poly.append(exps)
    return poly

def mult(a,b):
   """Returns the array resulting of element-wise multiplying two arrays"""
   return list(map(lambda element_a, element_b: element_a * element_b,a,b))

def add(a,num_to_add):
   """Returns the array resulting of adding the value of num_to_add to each element of the array"""
   return [element_a+num_to_add for element_a in a]  

def get_derivative(poly):
   """Returns the derivative of a polynomial using the power rule, 
      the polynomial is defined as an array of coefficients and exponents, 
      where coeficients is an array of floats and exponents is an array of integers.
      "poly" has the following structure [[cohefficients],[exponents]]
      example: 
      2x3 + 4x2 + -1.5x6 -> [[2,4,-1.5],[3,2,6]]
   """
   print("Calculating derivative...")
   coefs,exps = get_coefs_exps(poly)
   #calculating the derivate coefs by mulply coefs by exps
   derivate_coefs = mult(coefs,exps)
   #calculating the derivate exps by substracting 1 to original exps
   derivate_exps = add(exps,-1)
   #contruct a polynomial representation from the results
   deriv = construct_poly(derivate_coefs,derivate_exps)
   return deriv

def evaluate_poly(poly,x_value):
   """Evalute a polynomial function at a given point"""
   print("Evaluating polynomial...")
   coefs,exps = get_coefs_exps(poly)
   #Evaluating each term cx^e and adding them all
   result = sum(list(map(lambda c,e: c * x_value**e,coefs,exps)))
   return result

def poly_to_string(poly):
   """Transforms a polynomial expression defined as a list of [coefficients,exponents] to a string"""
   coefs,exps = get_coefs_exps(poly)
   result= " + ".join([str(coefs[i]) + "xˆ" + str(exps[i]) for i in range(len(coefs))])
   return result 
	
def test_derivative(poly,x_value):
    print("f(x) = " + poly_to_string(poly))
    deriv = get_derivative(poly)
    print("f'(x) = " + poly_to_string(deriv))
    slope = evaluate_poly(deriv,x_value)
    print("f'(" + str(x_value) + ") = " + str(slope))
    