import csv
import json

with open("OBSERVATION_MATRIX.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

ranks = [int(r["observed_rank"]) for r in rows]
names = [r["person"] for r in rows]

assert ranks == list(range(1, 11)), ranks
assert len(names) == len(set(names)) == 10

with open("RESULTS.json", encoding="utf-8") as f:
    results = json.load(f)

result_names = [x["person"] for x in results["observedRanking"]]
assert result_names == names
assert results["isOfficialOpenAIRanking"] is False
assert results["isCurrentChatGPTRanking"] is False

with open("CROSSWALK_INDEX_T001.csv", encoding="utf-8-sig", newline="") as f:
    crosswalk = list(csv.DictReader(f))

overlap = [r["person"] for r in crosswalk if r["in_index_t001"] == "да"]
assert overlap == ["Алексей Яковлев", "Максим Мельников", "Александр Тригуб"]
assert results["overlapWithIndexT001"]["count"] == len(overlap)

print("OK: historical observation, ordering and INDEX-T001 overlap are internally consistent")
