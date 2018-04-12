# coding: utf-8
# In[89]:
def scale(data,factor):
    n=len(data)
    for i in range(n):
        data[i]*=factor
my_list_1=["1","2",3,4,5]
scale(my_list_1,5)
my_list_1

# In[57]:
from random import randint

def create_n_random_numbers_to_be_inserted_tree(size):
    my_vector=[]
    for i in range(size):
        my_vector.append(randint(-500,500))
    print(my_vector)
    return my_vector
    
def BinaryTree(r=0):
    return [0, [], []]
    
def insertData(tree_root,data):
    if(tree_root[0]==None):
        tree_root=[0,[],[]]
        return 
    if(tree_root is not None and tree_root!=[]):
        
        if(tree_root[0]>data and tree_root[1]==[]):
            tree_root[1]=[data,[],[]]
        elif(tree_root[0]>data and tree_root[1]!=[]):
            insertData(tree_root[1],data)
        
        elif(tree_root[0]<data and tree_root[2]==[]):
            tree_root[2]=[data,[],[]]
        elif(tree_root[0]<data and tree_root[2]!=[]):
            insertData(tree_root[2],data)  
    else:
        print(" duplicate  .... ")
        
def prety_print(tree, depth=0):
    ret = ""

    # Print right branch
    if tree[2] != []:
        ret += prety_print(tree[2],depth + 1)

    # Print own value
    ret += "\n" + ("    "*depth) + str(tree[0])

    # Print left branch
    if tree[1] != []:
        ret += prety_print(tree[1],depth + 1)
    
    return ret
    
 def get_minimum_of_the_tree(tree_pass_parameter):
    tree_root=tree_pass_parameter
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[1]==[]):
            return tree_root[0]
        else:
            return get_minimum_of_the_tree(tree_root[1])
            
def get_maximum_of_the_tree(tree_pass_parameter):
    tree_root=tree_pass_parameter
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[2]==[]):
            #print("şu an max da  : ",tree_root[2])
            return tree_root[0]
        else:
            #print("şu an ilerliyor : ",tree_root[2])
            return get_maximum_of_the_tree(tree_root[2])    
            
def traverse_the_tree(tree,depth=0):
    global sum_of_the_depth_for_all_nodes
    # sum_of_the_depth_for_all_nodes=0
    tree_root=tree
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[1]==[]):
            pass
            #print(tree_root[0],",",end="")
        else:
            depth=depth+1
            traverse_the_tree(tree_root[1],depth)  
    if (tree_root is not None and tree_root!=[]):
        print(tree_root[0],",",end="")
        sum_of_the_depth_for_all_nodes=sum_of_the_depth_for_all_nodes+depth
        
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[2]==[]):
            pass
            #print(tree_root[0],",",end="")
        else:
            traverse_the_tree(tree_root[2],depth)
    #return sum_of_the_depth_for_all_nodes       
    
def find_data_on_tree(tree,data,position="0"): 
    tree_root=tree
    #print("tree : ",tree)
    #print("data :",data)
    #print()
    if (tree_root is not None and tree_root!=[]):
        if(tree_root[0]==data):
            print("found on",position)
            print(tree_root[0],",",end="")
            return position
        elif (tree_root[1]!=[] and data<tree_root[0]):
            find_data_on_tree(tree_root[1],data,position+"1")
        elif (tree_root[2]!=[] and data>tree_root[0]):
            find_data_on_tree(tree_root[2],data,position+"2")
            
    else:
        print("not found ")
        return 0

# In[71]:
r=BinaryTree()
agacta_kac_sayi_var=10
my_numbers=create_n_random_numbers_to_be_inserted_tree(agacta_kac_sayi_var)
for i in my_numbers:
    insertData(r,i)
## print(prety_print(r))
max=get_maximum_of_the_tree(r)
min=get_minimum_of_the_tree(r)
max,min
print(prety_print(r))
sum_of_the_depth_for_all_nodes=0  
traverse_the_tree(r)
sum_of_the_depth_for_all_nodes

# In[65]:
r

# In[66]:
find_data_on_tree(r,-38)

# In[67]:
r=None
my_list=[]
r=BinaryTree(0)
my_numbers=create_n_random_numbers_to_be_inserted_tree(15)
for i in my_numbers:
    insertData(r,i)
## print(prety_print(r))
max=get_maximum_of_the_tree(r)
min=get_minimum_of_the_tree(r)

min,max
traverse_the_tree(r)

#-------------------------------------------------------

# coding: utf-8
# In[3]:
# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys
 
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]
 
    # m[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            
            m[i][j] = sys.maxsize    #  previously sys.maxint in original code from https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
            for k in range(i, j):
 
                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
 
    return m[1][n-1]

# In[4]:
# Driver program to test above function
arr = [1, 2, 3 ,4]
size = len(arr)
print("Minimum number of multiplications is " +
       str(MatrixChainOrder(arr, size)))
# This Code is contributed by Bhavya Jain

# In[57]:
class My_Matrix():
    matrix=None
    def __init__(self,m=5,n=5,value=-1):
        from random import randint 
        matrix_list_of_list=[]
        low=0
        high=100
        for i in range(m):
            row_list=[]
            for j in range(n):
                if value==-1:
                    row_list.append(randint(low,high))
                else:
                    row_list.append(value)
                    
            matrix_list_of_list.append(row_list) 
            
        self.matrix=matrix_list_of_list
        
    def prety_print(self):
        m=len(self.matrix)
        n=len(self.matrix[0])
        print()
        print("  ************************************************** " )
        print("dimension is :",m,n)
        print("            ",end="")
        for i in range(len(self.matrix[0])):
            print(i," ",end="")
        print(end="\n")
        for i in range(len(self.matrix)):
            print("row ",i," : ",self.matrix[i])
        print(" ----------------------------------------------------------" )
        
    def get_row_i(self,i):
        return self.matrix[i]
        
    def get_column_i(self,i):
        col_i=[[x[i]] for x in m_1.matrix]
        return col_i
        
    def matrix_addition(self,matrix_2):
        m=len(self.matrix)
        n=len(self.matrix[0])
        for i in range(m):
            for j in range(n):
                self.matrix[i][j]=self.matrix[i][j]+matrix_2.matrix[i][j]     
                
    def matrix_subraction(self,matrix_2):
        m=len(self.matrix)
        n=len(self.matrix[0])
        for i in range(m):
            for j in range(n):
                self.matrix[i][j]=self.matrix[i][j]-matrix_2.matrix[i][j]    
                
    def matrix_scalar_multiplication(self,alpha):
        m=len(self.matrix)
        n=len(self.matrix[0])
        for i in range(m):
            for j in range(n):
                self.matrix[i][j]=self.matrix[i][j]*alpha
 
def test_matrix():
    m_1=My_Matrix(m=3,n=4,value=1)
    m_1.prety_print()
    
    m_2=My_Matrix(m=3,n=4)
    m_2.prety_print()
        
test_matrix()  

# In[ ]:
def matrix_vector_multiplication(matrix->My_Matrix,vector->My_Vector):
    matrix.
    b=[]
    b.
    for 

# In[60]:
m_1=My_Matrix()
m_1.prety_print()

m_1.matrix_scalar_multiplication(5)
m_1.prety_print()

# In[62]:
m_1=My_Matrix()
m_1.prety_print()

m_2=My_Matrix()
m_2.prety_print()

m_1.matrix_addition(m_2)
m_1.prety_print()

m_1.matrix_subraction(m_2)
m_1.prety_print()

# In[55]:
m_1.get_row_i(1)

# In[56]:
m_1.get_column_i(1)

# In[104]:
class My_Vector():
    vector=None
    size=None     
    
    def __init__(self,n=5,value=0,low=0,high=10):
        from random import randint
        self.vector=[]
        if(value is "random" or value is "r"):
            for i in range(n):
                self.vector.append([randint(low,high)])
                self.size=(n,1)
        else:
            for i in range(n):
                self.vector.append([value])
                self.size=(n,1)
                
    def scalar_multiplication(self,alpha=1):
        m=self.size[0]
        for i in range(m):
            self.vector[i][0]=self.vector[i][0]*alpha
            #  self.vector[i][0]=self.vector[i][0]*alpha,error if array 5x1, nx1 then access array[i] instead of array[i][0]
            # düzeldi ... 
            
    def vectorel_addition(self,vector_2):
        if(self.size!=vector_2.size):
            print("they should be same size ")
            return 
        m=self.size[0]
        for i in range(m):
            #   print(self.size)     
            #   print(vector_2.size)
            self.vector[i][0]=self.vector[i][0]+vector_2.vector[i][0]
            
    def vector_inner_product(self,vector_2):
        result=0
        if(self.size!=vector_2.size):
            print("not same dim in vectors")
            return 
        else:
            for i in range(self.size[0]):
                result=result+self.vector[i][0]*vector_2.vector[i][0]
            return result
    
    def get_m_n(self):
        print("dimension : ",self.size)
        return self.size
        
    def pprint(self):
        if(self.vector is None):
            print("not yet initialize")
        else:
            for i in range(len(self.vector)):
                print(self.vector[i])  
                
def test_vector():
    v_1=My_Vector(2,2)
    v_1.get_m_n()
    v_1.pprint()

    v_2=My_Vector(2,'r')
    v_2.get_m_n()
    v_2.pprint()

    v_1.vectorel_addition(v_2)
    v_1.get_m_n()
    v_1.pprint()
    
    a=v_1.vector_inner_product(v_2)
    print("inner product : ",a)
test_vector()

# In[99]:
v_2.vector

# In[97]:
from random import randint

def create_vector(size):
    my_vector=[]
    for i in range(size):
        my_vector.append(randint(0,50))
    return my_vector
    
def vector_inner_product(v1,v2):
    result=0
    if(len(v1)!=len(v2)):
        print("not same dim in vectors")
        return 
    else:
        for i in range(len(v1)):
            result=result+v1[i]*v2[i]
        return result
        
def create_matrix(m,n):
    my_matrix=[]
    for i in range(m):
        my_matrix.append(create_vector(n))
    return my_matrix
    
def matrix_multiplication(a,b):
    m=len(a)
    n_1=len(a[0])
    n_2=len(b)
    p=len(b[0])
    my_matrix=create_matrix(m,p)
    for i in range(m):
        for j in range(p):
            row_a=a[i]
            col_b=[row[j] for row in b]
            my_matrix[i][j]=vector_inner_product(row_a,col_b)
    return my_matrix
    
def matrix_pprint(m):
    print("------------------------")
    for i in range(len(m)):
        print(m[i])
    print("------------------")
    
def matrix_pprint_loop(m):
    i=0
    #print("---------------------------------------------------------")
    for item in m:
        print(" item : ",i)
        i=i+1
        matrix_pprint(item)      
    #print("--------------------------------------------------------")
v_1=create_vector(4)
m_1=create_matrix(2,7)
v_1,m_1

# In[46]:
m_2=create_matrix(2,2)
m_2

# In[47]:
c_1=[row[1] for row in m_2]
c_1

# In[61]:
m_1=create_matrix(2,3)
m_2=create_matrix(3,2)
m_3=matrix_multiplication(m_1,m_2)

matrix_pprint(m_1)
matrix_pprint(m_2)
matrix_pprint(m_3)

# In[35]:
matrix_pprint(m_2)

# In[36]:
matrix_pprint(m_3)

# In[16]:
# row_i_th=matrix[i]
m_1[1]

# In[17]:
# col_i_th=[row[i] for row in matrix]
col_3_th=[row[3] for row in m_1]
col_3_th

# In[5]:
v1=create_vector(5)
v2=create_vector(5)
x=vector_inner_product(v1,v2)
v1,v2,x

# In[64]:
m_1=create_matrix(4,4)
matrix_pprint(m_1)

# In[72]:
m=4
n=4
a=zip(range(m),range(n))
a
for item in a:
    print(item)

# In[74]:
indices_for_lower_part=[(i,j) for i in range(m) for j in range(n) if i>j]
matrix_pprint(indices_for_lower_part)

# In[88]:
import copy

def matrix_transform_it_to_lower_triangular(matrix_1):
    matrix=copy.deepcopy(matrix_1)
    m=len(matrix)
    n=len(matrix)
    indices_for_lower_part=[(i,j) for i in range(m) for j in range(n) if i>j]
    for i,j in indices_for_lower_part:
        matrix[i][j]=0
    return matrix
    
def matrix_transform_it_to_upper_triangular(matrix_1):
    matrix=copy.deepcopy(matrix_1)
    m=len(matrix)
    n=len(matrix)
    indices_for_lower_part=[(i,j) for i in range(m) for j in range(n) if i<j]
    for i,j in indices_for_lower_part:
        matrix[i][j]=0
    return matrix

# In[90]:
m_1=create_matrix(4,4)
matrix_pprint(m_1)

m_2=matrix_transform_it_to_lower_triangular(m_1)    #  or m_1=matrix_transform_it_to_lower_triangular(m_1)
matrix_pprint(m_2)
matrix_pprint(m_1)

m_3=matrix_transform_it_to_upper_triangular(m_1)    #  or m_1=matrix_transform_it_to_lower_triangular(m_1)
matrix_pprint(m_3)
matrix_pprint(m_1)

# In[98]:
m_1=create_matrix(3,1)
m_2=create_matrix(1,3)
m_3=matrix_multiplication(m_1,m_2)
matrix_pprint_loop([m_1,m_2,m_3])

# In[99]:
m_1=create_matrix(1,3)
m_2=create_matrix(3,1)
m_3=matrix_multiplication(m_1,m_2)
matrix_pprint_loop([m_1,m_2,m_3])

# In[87]:
v_1.vector[0][0]

# In[86]:
v_2.vector
