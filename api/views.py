from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.Serializer import*

from api.models import Books


class Products(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'msg':'inside product gate'})

class Morning(APIView):
    def morning(self,request,*args,**kwargs):
        return Response({'msg':'Good morning'})


class Productview(APIView):
      def post(self,request,*args,**kwargs):
          serializer=BookSerializer(data=request.data)
          if serializer.is_valid():
              Books.objects.create(**serializer.validated_data)
              return Response(data=serializer.data)
          else:
              return Response(data=serializer.errors)

      def get(self,request,*args,**kwargs):
          qs=Books.objects.all()
          serializer=BookSerializer(qs,many=True)
          return Response(data=serializer.data)

class Productdetailsview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book,many=False)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Books.objects.get(id=id).delete()
        return Response(data="deleted")

    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

class ReviewsView(APIView):
    def get(self,request,*args,**kwargs):
        review=Reviews.objects.all()
        serializer=ReviewModelSerializer(review,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ReviewModelSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

class ReviewDetails(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        qs=Reviews.objects.get(id=id)
        serializer=ReviewModelSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        object=Reviews.objects.get(id=id)
        serializer=ReviewModelSerializer(instance=object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Reviews.objects.get(id=id).delete()
        return Response("deleted")








class Add(APIView):
    def post(self,request,*args,**kwargs):
        a=int(request.data.get('num1'))
        b=int(request.data.get('num2'))
        sum=a+b

        return Response({'msg':sum})

class MUL(APIView):
       def get(self,request,*args,**kwargs):
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
        res=num1*num2
        return Response({'result':res})
class SUB(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get('num1')
        n2=request.data.get('num2')
        diff=int(n1)-int(n2)
        return Response({'dif':diff})
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get('num1'))
        cube=n1**3
        return Response({'res':cube})
class Numcheck(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get('num1'))
        if n1%2==0:
            res="number is even"
        elif n1%2==1:
            res="number is odd"
        return Response(data=res)

class Fact(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num1'))
        s=1
        for i in range(1,n+1):
            s=i*s
        return Response({'res':s})
class Wordcount(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        lst=text.split(' ')
        print(lst)
        word={}
        for i in lst:
            a=lst.count(i)
            word={i:a}
            print(word)

        return Response(data=a)
class Pali(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get('text')
        print('text is',txt)
        l=len(txt)
        str=''
        print(l)
        str=str+txt[::-1]
        print('string is',str)
        if str==txt:
            return Response(data='palindrome')
        else:
            return Response(data='not palindrome')

class Armstrong(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num1'))
        sum=0
        temp=n
        while temp>0:
            b=temp%10
            sum=sum+b**3
            temp=temp//10
        if sum==n:
            return Response(data='number is armstrong')
        else:
            return Response(data='number is not armstrong')
class Prime(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num1'))
        flag=0
        for i in range(2,n-1):
            if (n%i)==0:
                flag=True
                break
        if flag:
                return Response(data='number is not prime')
        else:
            return Response(data='number is  prime')
