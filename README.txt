Hello. This is my take in the challenge https://github.com/luuna-tech/test/tree/master/backend

I tried to keep it simple in order to avoid complexity in the revision, so instead of pasing an .env local
with variables and then importing them to settings I decided to just leave secret_key and smtp key there. 
Since this is a test project those keys are not really important

app is deployed to https://hlombardo-zebrands.herokuapp.com/api/stockmanager/ and I went ahead and created 2 users,
one admin and one test user.

You can use this API with postman using 

https://hlombardo-zebrands.herokuapp.com/api/stockmanager/products/ as url and it has a simple token Auth so you must
set the headers to 

Key           value
Authorization Token 8392b99adbaf4ec033827c5d97acc08d8fb26dbf     | for admin
Authorization Token 7507bc10de13a8ac790936e343c8d506b5c12d97     | for test user

as requested only admins can edit, create or delete products. Users can only see they info (minus pk and the 
anonymous get counter) and admins will aslo receive an email inforing about changes when a product is updated.

