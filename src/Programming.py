------------------------------------
# ex3-0.sh
#!/bin/sh

echo Hello World
------------------------------------
# ex3-1.sh
#!/bin/sh

i=0;

while [ "$i" -lt "$1" ];
do
        echo "hello world";
        i=$((i + 1));
done
------------------------------------
# ex3-2.sh
#!/bin/sh

[ "$#" -eq 3 ] || exit 1
echo $(( $1 $2 $3 ))
------------------------------------
# ex3-3.sh
#!/bin/sh

weight=$1
height_cm=$2
height_m=$(echo "scale=2; $height_cm / 100" | bc)
bmi=$(echo "scale=1; $weight / ($height_m * $height_m)" | bc)

if [ "$(echo "$bmi < 18.5" | bc)" -eq 1 ]; then
    echo "저체중입니다."
elif [ "$(echo "$bmi >= 18.5 && $bmi < 23" | bc)" -eq 1 ]; then
    echo "정상 체중입니다."
else
    echo "과체중입니다."
fi
------------------------------------
# ex3-4.sh
#!/bin/sh

echo "리눅스가 재밌나요? (Yes / No)"
read answer

case "$answer" in
    [Yy]*)
        echo "yes"
        ;;
    [Nn]*)
        echo "no"
        ;;
    *)
        echo "yes or no로 입력해 주세요."
        ;;
esac
------------------------------------
# ex3-5.sh
#!/bin/sh

my_ls() {
    ls "$@"
}

echo "프로그램을 시작합니다."

my_ls "$@"
------------------------------------
# ex3-6.sh
#!/bin/sh

FOLDER_NAME="files"

if [ ! -d "$FOLDER_NAME" ]; then
    echo "$FOLDER_NAME 폴더를 생성합니다."
    mkdir "$FOLDER_NAME"
fi

cd "$FOLDER_NAME"

for i in 0 1 2 3 4; do
    touch "file$i.txt"
done

tar -cvf files.tar file*.txt

echo "$FOLDER_NAME files.tar 압축 완료"
------------------------------------
# ex3-7.sh
#!/bin/sh

folder_name=$1

if [ ! -d "$folder_name" ]; then
    mkdir "$folder_name"
fi

cd "$folder_name"
for i in $(seq 0 4); do
    touch "file$i.txt"
done

for i in $(seq 0 4); do
    mkdir -p "file$i"
    ln -s "$(pwd)/file$i.txt" "file$i/file$i.txt"
------------------------------------
# ex3-8.sh
#!/bin/sh

if [ $# -ne 2 ]; then
    echo "Usage: sh ./ex3-8.sh [Name] [Phone/Birthday]"
    exit 1
fi

name=$1
info=$2

if ! grep -q "\-\-my friends\-\-" DB.txt; then
    echo "--my friends--" > DB.txt
fi

echo "$name $info" >> DB.txt
------------------------------------
# ex3-9.sh
#!/bin/sh

if [ $# -ne 1 ]; then
    echo "Please provide a name to search."
    exit 1
fi

grep -i "$1" DB.txt
------------------------------------
