#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

static int sum = 0;

struct Node{
  int data;
  struct Node *left,*right;
};

struct Node *addNode(struct Node *root,int data){
    if(root==NULL){
        struct Node *tmp = (struct Node*)malloc(sizeof(struct Node));
        tmp->data = data;
        tmp->left = NULL;
        tmp->right = NULL;
        return tmp;
    }
    if(root->data < data){
        root->right = addNode(root->right,data);
    }else{
       root->left = addNode(root->left,data);
    }
    return root;
}

void Print(struct Node *root){
    if(root){
        printf("%d ",root->data);
        Print(root->left);
        Print(root->right);
    }
}

int minimum(struct Node *root){
  if(root->left == NULL){
    return root->data;
  }
  return minimum(root->left);
}

int maximum(struct Node *root){
  if(root->right == NULL){
    return root->data;
  }
  return maximum(root->right);
}

int nodeNumber(struct Node *root){
    if(root==NULL) return 0;
    return 1+nodeNumber(root->left)+nodeNumber(root->right);
}

int depth(struct Node * root){
    if(root==NULL) return 0;
    else{
        int left_height=0, right_height=0;
        left_height=depth(root->left);
        right_height=depth(root->right);
        if(right_height>left_height){
            return right_height+1;
        }
        else{
            return left_height+1;
        }
    }
}

int summaryDepth(struct Node * root){
    if(root==NULL) return 0;
    int depthValue = depth(root)-1;
    int i, summary=0;
    for(i=depthValue; i>=0; i--){
        summary += i;
    }
    return summary;
}

void summaryDepth2(struct Node *root, int depthValue){
    if(root==NULL) return;
    if(root->right != NULL || root->left != NULL){
    	depthValue++;
    	if(root->left != NULL){
    		sum += depthValue;
    		summaryDepth2(root->left,depthValue);
		}
		if(root->right != NULL){
    		sum += depthValue;
    		summaryDepth2(root->right,depthValue);
		}
	}
}

int search(struct Node *root, int val){
    while (root != NULL) {
        if (val == root->data) {
            return 1;
        }
        if (val < root->data) {
            root = root->left;
        } else {
            root = root->right;
        }
    }
    return 0;
}

int main(){

  struct Node *root=NULL;

  int randomNumber;
  srand(time(NULL));

  int i, number;
  printf("\n\tEnter Node Value: ");
  scanf("%d", &number);

  for(i=0; i<number; i++){
    randomNumber=1+rand()%100;
    root = addNode(root,randomNumber);
  }

  printf("\n\t");
  Print(root);
  printf("\n\n\tMinimum \t: %d",minimum(root));
  printf("\n\tMaximum \t: %d",maximum(root));
  printf("\n\tNode Number \t: %d",nodeNumber(root));
  printf("\n\tDepth \t\t: %d",depth(root)-1);
  printf("\n\tSum Depth-Line \t: %d",summaryDepth(root));
  summaryDepth2(root,0);
  printf("\n\tSum Depth-All \t: %d\n",sum);
  getch();
  //printf("\nSearch (25) = %d",search(root,25));
  return 0;
}
