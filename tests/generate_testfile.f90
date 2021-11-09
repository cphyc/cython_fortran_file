program generate_testfile
    implicit none
    integer :: unit
    real(4) :: x4(2)
    real(8) :: x8(2)
    integer(4) :: i4(2), ishort
    integer(8) :: i8(2), ilong

    open(file="testfile.bin", newunit=unit, form="unformatted")

    x4 = (/1e0, 2e0/)
    x8 = (/3d0, 4d0/)
    i4 = (/5, 6/)
    i8 = (/7, 8/)
    ishort = 1234
    ilong = 123456789
    ! Write scalars
    write(unit) ishort
    write(unit) ilong
    write(unit) 1e0
    write(unit) 2d0

    ! Write vectors
    write(unit) i4
    write(unit) i8
    write(unit) x4
    write(unit) x8
end program