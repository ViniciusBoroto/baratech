package utils

// SlicePop pops an element from a slice and returns the new slice and element.
//
// SlicePop modifies the slice. To preserve the original slice, make a copy.
//
//   arr := []int{1, 2, 3}
//   arr, elem := SlicePop(arr, 1)
//   fmt.Println(arr, elem) // [1 3] 2
func SlicePop[T any](s []T, i int) ([]T, T) {
	elem := s[i]
	s = append(s[:i], s[i+1:]...)
	return s, elem
}
