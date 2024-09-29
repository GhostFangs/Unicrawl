import argparse
from pddiktipy import api
from pprint import pprint as p

a = api()



parser = argparse.ArgumentParser(description="Data search program using PDDIKTI API")

parser.add_argument("keyword", nargs="?", help="General search across all categories", type=str)
parser.add_argument("-m", "--mahasiswa", help="Search for students based on given keyword", type=str)
parser.add_argument("-d", "--dosen", help="Search for lecturers based on given keyword", type=str)
parser.add_argument("-pt", help="Search for universities based on given keyword", type=str)
parser.add_argument("-p", "--prodi", help="Search for study programs based on given keyword", type=str)
parser.add_argument("-md", "--mhs_detail", help="Get detail of student data based on ID", type=str)
parser.add_argument("-dpf", "--dosen_profile", help="Get detail of lecturer data based on ID", type=str)
parser.add_argument("-dpn", "--dosen_penelitian", help="Get lecturer research data based on lecturer's ID", type=str)
parser.add_argument("-da", "--dosen_pengabdian", help="get lecturer dedication data based on lecturer's ID", type=str)
parser.add_argument("-dk", "--dosen_karya", help="Get lecturer work data based on lecturer's ID", type=str)
parser.add_argument("-dp", "--dosen_paten", help="get lecturer patent data based on lecturer's ID", type=str)
parser.add_argument("-dsh", "--dosen_study_history", help="get lecturer study history based on lecturer's ID", type=str)
parser.add_argument("-dth", "--dosen_teaching_history", help="get lecturer teaching history based on lecturer's ID", type=str)
parser.add_argument("-ptd", "--pt_detail", help="Get university details by ID", type=str)
parser.add_argument("-ptp", "--pt_prodi", help="Get study program data at a particular university based on ID and academic year", type=str)
parser.add_argument("-ptl", "--pt_logo", help="Get university logo by ID and Return it as base64 encoded string", type=str)
parser.add_argument("-ptr", "--rasio_pt", help="Get study program data at a specific university based on ID and academic year", type=str)
parser.add_argument("-mpt", "--mahasiswa_pt", help="get student data at a particular university based on ID", type=str)
parser.add_argument("-ptw", "--pt_waktu_studi", help="get data on average study time of students at a particular university based on ID", type=str)
parser.add_argument("-ptn", "--pt_name_history", help="get university name history by ID", type=str)
parser.add_argument("-ptc", "--pt_cost", help="get the estimated tuition fees at a particular university based on ID", type=str)
'''parser.add_argument("-ptgr", "--pt_graduation_rate", help="", type=str)'''
'''parser.add_argument("-gjrp", "--get_jumlah_prodi_pt", help="", type=str)'''
'''parser.add_argument("-gjmp", "--get_jumlah_mahasiswa_pt", help="", type=str)'''
'''parser.add_argument("-gsfnp", "--get_sarpras_file_name_pt", help="", type=str)'''
'''parser.add_argument("-gsbp", "--get_sarpras_blob_pt", help="", type=str)'''
'''parser.add_argument("-gdpr", "--get_detail_prodi", help="", type=str)'''
'''parser.add_argument("-gepr", "--get_desc_prodi", help="", type=str)'''
'''parser.add_argument("-gnhp", "--get_name_histories_prodi", help="", type=str)'''
'''parser.add_argument("-", "--get_num_students_lecturers_prodi", help="", type=str)'''

args = parser.parse_args()

if args.keyword:
    print(f"Searching all data across all categories for: {args.keyword}")
    result = a.search_all(args.keyword)
    if result:
        p(result)
    else:
        print(f"No data was found for: {args.keyword}")

elif args.mahasiswa:
    print(f"Searching for student data for: {args.mahasiswa}")
    result = a.search_mahasiswa(args.mahasiswa)
    if result:
        p(result)
    else:
        print(f"No student data was found for: {args.mahasiswa}")

elif args.dosen:
    print(f"Searching for lecturer data for: {args.dosen}")
    result = a.search_dosen(args.dosen)
    if result:
        p(result)
    else:
        print(f"No lecturer data found for: {args.dosen}")

elif args.pt:
    print(f"Searching for universities data for: {args.pt}")
    result = a.search_pt(args.pt)
    if result:
        p(result)
    else:
        print(f"No universities data was found for: {args.pt}")

elif args.prodi:
    print(f"Searching for Prodi data for: {args.prodi}")
    result = a.search_prodi(args.prodi)
    if result:
        p(result)
    else:
        print(f"No universities data was found for: {args.search_prodi}")

elif args.mhs_detail:
    print(f"Searching for details of a student for: {args.mhs_detail}")
    result = a.get_detail_mhs(args.mhs_detail)
    if result:
        p(result)
    else:
        print(f"No student detail for: {args.mhs_detail}")

elif args.dosen_profile:
    print(f"Searching for details of a lecturer for: {args.dosen_profile}")
    result = a.get_dosen_profile(args.dosen_profile)
    if result:
        p(result)
    else:
        print(f"No lecturer detail for: {args.dosen_profile}")

elif args.dosen_penelitian:
    print(f"Searching for lecturer research for: {args.dosen_penelitian}")
    result = a.get_dosen_penelitian(args.dosen_penelitian)
    if result:
        p(result)
    else:
        print(f"No lecturer research data for: {args.dosen_penelitian}")

elif args.dosen_pengabdian:
    print(f"Searching for lecturer dedication data for: {args.dosen_pengabdian}")
    result = a.get_dosen_pengabdian(args.dosen_pengabdian)
    if result:
        p(result)
    else:
        print(f"No lecturer's detail found for: {args.dosen_pengabdian}")

elif args.dosen_karya:
    print(f"Searching for lecturer's work data for: {args.dosen_karya}")
    result = a.get_dosen_karya(args.dosen_karya)
    if result:
        p(result)
    else:
        print(f"No data found on lecturer's work for: {args.dosen_karya}")

elif args.dosen_paten:
    print(f"Searching for lecturer's patent data for: {args.dosen_paten}")
    result = a.get_dosen_paten(args.dosen_paten)
    if result:
        p(result)
    else:
        print(f"No data found on lecturer's patent for: {args.dosen_paten}")

elif args.get_dosen_study_history:
    print(f"Searching for lecturer's patent data for: {args.dosen_study_history}")
    result = a.get_dosen_patenget_dosen_study_history(args.dosen_study_history)
    if result:
        p(result)
    else:
        print(f"No data found on lecturer's study history for: {args.dosen_study_history}")

elif args.dosen_teaching_history:
    print(f"Searching for lecturer's teaching history for: {args.dosen_teaching_history}")
    result = a.get_dosen_teaching_history(args.dosen_teaching_history)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.dosen_teaching_history}")

elif args.pt_detail:
    print(f"Searching for university data for: {args.pt_detail}")
    result = a.get_detail_pt(args.pt_detail)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_detail}")

elif args.pt_prodi:
    print(f"Searching for university data for: {args.pt_prodi}")
    result = a.get_prodi_pt(args.pt_prodi)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_prodi}")

elif args.pt_logo:
    print(f"Searching for university logo for: {args.pt_logo}")
    result = a.get_logo_pt(args.pt_logo)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_logo}")

elif args.pt_rasio:
    print(f"Searching for student to faculty ratio data for: {args.pt_rasio}")
    result = a.get_rasio_pt(args.pt_rasio)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_rasio}")

elif args.mahasiswa_pt:
    print(f"Searching for student at a particular university for: {args.mahasiswa_pt}")
    result = a.get_mahasiswa_pt(args.mahasiswa_pt)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.mahasiswa_pt}")

elif args.pt_waktu_studi:
    print(f"Searching for university data for: {args.pt_waktu_studi}")
    result = a.get_waktu_studi_pt(args.pt_waktu_studi)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_waktu_studi}")

elif args.pt_name_history:
    print(f"Searching for university data for: {args.pt_name_history}")
    result = a.get_name_histories_pt(args.pt_name_history)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_name_history}")

elif args.pt_graduation_rate:
    print(f"Searching for university data for: {args.pt_graduation_rate}")
    result = a.get_graduation_rate_pt(args.pt_graduation_rate)
    if result:
        p(result)
    else:
        print(f"No data found for: {args.pt_graduation_rate}")

else:
    print("{'python Unicrawl.py --help' will help you out with all the commands}")
