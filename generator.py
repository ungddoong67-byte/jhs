
import os
import re

# 화성특례시 전 지역 퀵서비스 페이지 데이터
# 2026년 기준 4개 구 / 29개 읍·면·동 + 주요 배송 거점

hwaseong_data = [
    {
        "dist": "만세구",
        "towns": [
            # 읍·면·동
            "우정읍",
            "향남읍",
            "남양읍",
            "마도면",
            "송산면",
            "서신면",
            "팔탄면",
            "장안면",
            "양감면",
            "새솔동",

            # 주요 생활·산업 거점
            "향남1지구",
            "향남2지구",
            "남양뉴타운",
            "조암",
            "발안",
            "우정국가산업단지",
            "화성바이오밸리",
            "마도일반산업단지",
            "전곡해양산업단지",
            "송산그린시티",
            "궁평항",
            "제부도",
            "화성시청"
        ]
    },
    {
        "dist": "효행구",
        "towns": [
            # 읍·면·동
            "봉담읍",
            "매송면",
            "비봉면",
            "정남면",
            "기배동",

            # 주요 생활·산업 거점
            "봉담1지구",
            "봉담2지구",
            "봉담신도시",
            "수원대학교",
            "협성대학교",
            "어천역",
            "비봉지구",
            "정남산업단지",
            "화성봉담IC",
            "천천리"
        ]
    },
    {
        "dist": "병점구",
        "towns": [
            # 읍·면·동
            "진안동",
            "병점1동",
            "병점2동",
            "반월동",
            "화산동",

            # 주요 생활·산업 거점
            "병점역",
            "병점역세권",
            "병점복합타운",
            "진안신도시",
            "기산지구",
            "안녕동",
            "융건릉",
            "반월산업단지",
            "한신대학교"
        ]
    },
    {
        "dist": "동탄구",
        "towns": [
            # 읍·면·동
            "동탄1동",
            "동탄2동",
            "동탄3동",
            "동탄4동",
            "동탄5동",
            "동탄6동",
            "동탄7동",
            "동탄8동",
            "동탄9동",

            # 주요 생활·산업 거점
            "동탄신도시",
            "동탄역",
            "동탄역세권",
            "동탄테크노밸리",
            "동탄호수공원",
            "동탄산업단지",
            "삼성전자화성캠퍼스",
            "동탄일반산업단지",
            "동탄물류단지",
            "동탄대로",
            "동탄센트럴파크",
            "동탄여울공원",
            "동탄출장소"
        ]
    }
]


def safe_folder_name(name):
    """폴더명에 사용할 수 없는 문자 정리"""
    name = re.sub(r'[\\/:*?"<>|]', '', name)
    return name.strip()


def create_page(folder_name, town, town_full):
    """개별 페이지 생성"""
    folder = safe_folder_name(folder_name)
    os.makedirs(folder, exist_ok=True)

    content = (
        "---\n"
        "layout: board\n"
        f"town: {town}\n"
        f"town_full: {town_full}\n"
        "---\n"
    )

    file_path = os.path.join(folder, "index.html")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return file_path


def generate_hwaseong_pages():

    total_pages = 0
    created_folders = set()

    # 1. 화성시 전체 통합 페이지
    create_page(
        "화성퀵서비스",
        "화성",
        "경기도 화성시 전지역 당일 퀵서비스 신속한 배송"
    )

    total_pages += 1
    print("✔ 통합 페이지 생성: 화성퀵서비스")

    # 2. 4개 구별 페이지 및 읍·면·동·거점 페이지
    for group in hwaseong_data:

        dist_name = group["dist"]

        # 구별 통합 페이지
        dist_folder = f"{dist_name}퀵서비스"

        if dist_folder not in created_folders:
            create_page(
                dist_folder,
                dist_name,
                f"경기도 화성시 {dist_name} 전지역 퀵서비스 신속한 배송"
            )

            created_folders.add(dist_folder)
            total_pages += 1

            print(f"✔ 구역 페이지 생성: {dist_folder}")

        # 읍·면·동 및 주요 거점 페이지
        for town_name in group["towns"]:

            folder_name = f"{town_name}퀵서비스"

            # 중복 폴더 생성 방지
            if folder_name in created_folders:
                print(f"⚠ 중복 항목 건너뜀: {folder_name}")
                continue

            town_full = (
                f"경기도 화성시 {dist_name} "
                f"{town_name} 당일 퀵서비스 신속한 배송"
            )

            create_page(
                folder_name,
                town_name,
                town_full
            )

            created_folders.add(folder_name)
            total_pages += 1

            print(f"✔ 생성 완료: {folder_name}")

    print("\n" + "=" * 50)
    print("🚀 화성특례시 퀵서비스 페이지 생성 완료!")
    print("=" * 50)
    print(f"✅ 생성된 전체 페이지: {total_pages}개")
    print("✅ 화성시 통합 페이지: 화성퀵서비스")
    print("✅ 구별 페이지: 만세구 / 효행구 / 병점구 / 동탄구")
    print("✅ 읍·면·동 및 주요 거점 페이지 생성 완료")
    print("\n📌 GitHub에 업로드한 뒤 사이트 배포 상태를 확인하세요.")
    print("🌐 대상 도메인: 화성퀵서비스.5282quick.com")


if __name__ == "__main__":
    generate_hwaseong_pages()
