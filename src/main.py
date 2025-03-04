from agents.therapist import TherapistAgent
from agents.patient import PatientAgent
from memory.dialogue_context import DialogueContext

def main():
    therapist = TherapistAgent() # 心理医生 Agent
    patient = PatientAgent() # 患者 Agent
    context = DialogueContext() # 对话上下文

    print("----心理咨询会话开始----\n")

    # 第一轮：患者发起对话
    patient_msg = patient.start_conversation()
    print(f"患者: {patient_msg}")
    context.add_patient_response(patient_msg)

    # 进行多轮对话
    while True:
        # 心理医生回复
        therapist_response = therapist.respond(context.get_full_dialogue())
        print(f"\n心理医生: {therapist_response}")
        context.add_therapist_response(therapist_response)

        if should_end_session(therapist_response, is_therapist=True):
            break

        # 患者回复
        patient_response = patient.respond(context.get_full_dialogue())
        print(f"\n患者: {patient_response}")
        context.add_patient_response(patient_response)

        if should_end_session(patient_response, is_therapist=False):
            break

    print("\n【心理咨询会话结束】")

    # 打印完整对话记录
    print("\n完整对话记录：")
    for idx, entry in enumerate(context.get_full_dialogue(), 1):
        print(f"{idx}. {entry['speaker']}: {entry['content']}")

# 结束对话的条件
def should_end_session(response, is_therapist):
    ending_phrases = ["再见", "帮助", "谢谢"]
    return any(phrase in response for phrase in ending_phrases)

if __name__ == "__main__":
    main()