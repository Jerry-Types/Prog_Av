sumaRenglones::[Int]->[Int]->[Int]
sumaRenglones [] [] = []
sumaRenglones (x:xs) (y:ys) = x+y:sumaRenglones (xs) (ys)

cuadrados::[[Int]]->[[Int]]->[[Int]]
cuadrados l l2 = [sumaRenglones p q| p <-l,q<-l2]