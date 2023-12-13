import os
import streamlit as st
from openai import OpenAI

# Ensure your key is stored safely
api_key = st.secrets["OPENAI_KEY"]

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)

def paragraph_builder1(painpoint, reference, value, painsnippet, source):
    try:       
        response1 = client.chat.completions.create(
            model="gpt-4-1106-preview",
             messages=[
                {
                "role": "system",
                "content": "**Alasco Paragraph Writing Assistant**\n\n**Objective**: Craft an Alasco paragraph using user inputs.\n\n### Text Drafting Guidelines:\n\n**Core Principles**:\n- **Readability**: Prioritize clarity.\n- **Tone**: Stay formal.\n- **Content**: Retain the core message.\n- **Length**: Maximum of 70 words.\n- **Style**: Copy the writing style and tone from the examples below.\n- **Narrative**: Pursue a consistent storyline.\n- **Language**: German.\n\n**Specific Directives**:\n- **Theme**: Stick to one main topic.\n- **Perspective**: Avoid first-person ('I/ich') to maintain a formal tone.\n\n**Phrases & Approaches to Avoid**:\n- Avoid sounding promotional or overly complimentary.\n- Sidestep phrases like: 'als Anerkennung für ihre Zeit', ’Ich habe gehört’,’Ich habe zur Kenntnis genommen’, ‘Referenzbericht’, and 'Als Belohnung'.\n\n## Alasco Paragraph Framework Overview:\n\nThe framework consists of 5 parts, following this order:\n\n1. **Format**: Always starts with “Hier”\n2. **Reference**: Include a reference with a specific role\n3. **Pain Point**: Describe a pain point the reference has experienced.\n4. **Pain Reliever**: Mention the solution that helped the reference.\n5. **Closing Question**: Always conclude with: “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n## Required Inputs:\n\n- Format: [...]\n- Reference: [...]\n- Pain Point: [...]\n- Pain Reliever: [...]\n- Closing Question: “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n## Examples:\n\n\n\n# Example 1:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Fabian von Köppen - Geschäftsführer bei GARBE - \n- **Pain point:** Unstable Processes with Decentralized or Inadequate Data Management.\n- **Pain reliever:** Stabile Prozesse\n- **Pain Snippet:** durch stabile Prozesse und eine zentrale Datenbasis eine sichere Entscheidungsgrundlage besitzt und zusätzlich seinen Mitarbeitern ein effizienteres Arbeiten ermöglicht. \n\nInsbesondere ab Minute 00:25 wird auf diese und weitere Mehrwerte eingegangen. \n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, das zeigt wie Fabian von Köppen - Geschäftsführer bei GARBE - durch stabile Prozesse und eine zentrale Datenbasis eine sichere Entscheidungsgrundlage besitzt und zusätzlich seinen Mitarbeitern ein effizienteres Arbeiten ermöglicht. \n\nInsbesondere ab Minute 00:25 wird auf diese und weitere Mehrwerte eingegangen. \n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt?\n\n# Example 2:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Sven Seehawer (Geschäftsführer) und Robert Maaß (Teamleiter Projektcontrolling) von KVL \n- **Pain point:** \"Excel ist nicht nur langsam, sondern auch in Bezug auf die IT-Sicherheit fragwürdig und erzeugt Ängste\"\n- **Pain reliever:** Eigenständiger Zugriff auf individuell einstellbare Reporting-Ansicht basierend auf Echtzeit-Daten, kein Warten auf MA-Reportings\n- **Pain Snippet:** “das Warten auf MA-Reportings entfällt und ein neues Maß an Sicherheit und Kontrolle erreicht wird: \"Da habe ich klare Strukturen, es funktioniert immer gleich\".\n\nInsbesondere ab Minute 01:46 wird auf diese und weitere Mehrwerte eingegangen.\n\n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, das zeigt, wie Sven Seehawer (Geschäftsführer) und Robert Maaß (Teamleiter Projektcontrolling) von KVL durch den Einsatz einer Software mit klaren Strukturen, auf individuell einstellbare Reporting-Ansichten in Echtzeit zugreifen können, wodurch das Warten auf MA-Reportings entfällt und ein neues Maß an Sicherheit und Kontrolle erreicht wird: \"Da habe ich klare Strukturen, es funktioniert immer gleich\".\n\nInsbesondere ab Minute 01:46 wird auf diese und weitere Mehrwerte eingegangen.\n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt?\n\n# Example 3:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Torsten Hecht - Projektmanager bei der THOST Projektmanagement GmbH - \n- **Pain point:** Viel Kommunikation mit Projektbeteiligten via Meetings / Mails / Telefonate (Stress)\n- **Pain reliever:** Priorisierung von Aufgaben & Überblick über Fristen\n- **Pain Snippet:** \"riesigen E-Mail-Flut\", und \"irgendwelchen Telefonate\", überfordert war und den Überblick verlor. Durch den Einsatz von Alasco hat er nun eine verlässliche Echtzeit-Datengrundlage und zusätzlich eine Zeitersparnis von 75%  allein im Rechnungsprüfungslauf. \n\nInsbesondere ab Minute 01:30 wird auf diese und weitere Mehrwerte eingegangen.\n\n\n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, die beschreibt, wie Torsten Hecht - Projektmanager bei der THOST Projektmanagement GmbH - mit eine \"riesigen E-Mail-Flut\", und \"irgendwelchen Telefonate\", überfordert war und den Überblick verlor. Durch den Einsatz von Alasco hat er nun eine verlässliche Echtzeit-Datengrundlage und zusätzlich eine Zeitersparnis von 75%  allein im Rechnungsprüfungslauf. \n\nInsbesondere ab Minute 01:30 wird auf diese und weitere Mehrwerte eingegangen.\n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt? \n\n\n# Example 4:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Virom Subash - Head of Construction bei Kintyre - \n- **Pain point:** Mangelnder Überblick über Projektaufgaben sowie Fristen\n- **Pain reliever:** Minderung zeitintensiver Prozesse durch Workflows & automatisierte Datenübertragungen\n- **Pain Snippet:** und dank der Automatisierung, manuelle Aufgaben wie die Rechnungsabwicklung \"in einem ganz anderen Tempo\" erledigt.   \n\nInsbesondere ab Minute 01:25 wird auf diese und weitere Mehrwerte eingegangen. \n\n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, das zeigt wie Virom Subash - Head of Construction bei Kintyre - immer den Überblick über den Projektstatus hat, und dank der Automatisierung, manuelle Aufgaben wie die Rechnungsabwicklung \"in einem ganz anderen Tempo\" erledigt.   \n\nInsbesondere ab Minute 01:25 wird auf diese und weitere Mehrwerte eingegangen. \n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt? \n\n\n# Example 5:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Gudrun Piesczeck - Projektleiterin bei der Rosa-Alscher-Gruppe - \n- **Pain point:** Schwierige Vorausplanung von anfallenden Kosten um Engpässe und Überfinanzierung zu vermeiden\n- **Pain reliever:** Besser Vorausplanen: Individuell einstellbare Mittelabflussplanung verknüpft mit dem Rechnungsprüflauf\n- **Pain Snippet:** \n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** Hier ein interessantes Video, das zeigt, wie Gudrun Piesczek - Projektleiterin bei der Rosa-Alscher Gruppe - eine strukturierte Software mit Rechnung-Workflow einsetzt um alle ihre Projektkosten besser zu planen und verwalten zu können.\n\nEin Thema, das auch Sie aktuell beschäftigt? \n Never ever use the word: 'aufschlussreiches'"
                },
                {
                "role": "user",
                "content": f"## **Your Turn**: Start writing your text below using the provided guidelines and framework. \n\n## Required Inputs:  \n\nFormat: Video\nReference: {reference} \nPain point: {painpoint} \nPain reliever: {value} \nPain Snippet: {painsnippet} \nClosing question: “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n"
                }
            ],
            temperature=0.5,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response1 = response1.choices[0].message.content
        #st.write(response1)
        return response1
        
    except Exception as e:
        st.write(f"An error occurred: {e}")

def paragraph_builder2(painpoint, reference, value, painsnippet, source):
    try:       
        response2 = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
                messages=[
                {
                "role": "system",
                "content": "**Alasco Paragraph Writing Assistant**\n\n**Objective**: Craft an Alasco paragraph using user inputs.\n\n### Text Drafting Guidelines:\n\n**Core Principles**:\n- **Readability**: Prioritize clarity.\n- **Tone**: Stay formal.\n- **Content**: Retain the core message.\n- **Length**: Maximum of 70 words.\n- **Style**: Copy the writing style and tone from the examples below.\n- **Narrative**: Pursue a consistent storyline.\n- **Language**: German.\n\n**Specific Directives**:\n- **Theme**: Stick to one main topic.\n- **Perspective**: Avoid first-person ('I/ich') to maintain a formal tone.\n\n**Phrases & Approaches to Avoid**:\n- Avoid sounding promotional or overly complimentary.\n- Sidestep phrases like: 'als Anerkennung für ihre Zeit', ’Ich habe gehört’,’Ich habe zur Kenntnis genommen’, ‘Referenzbericht’, and 'Als Belohnung'.\n\n## Alasco Paragraph Framework Overview:\n\nThe framework consists of 5 parts, following this order:\n\n1. **Format**: Always starts with “Hier”\n2. **Reference**: Include a reference with a specific role\n3. **Pain Point**: Describe a pain point the reference has experienced.\n4. **Pain Reliever**: Mention the solution that helped the reference.\n5. **Closing Question**: Always conclude with: “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n## Required Inputs:\n\n- Format: [...]\n- Reference: [...]\n- Pain Point: [...]\n- Pain Reliever: [...]\n- Closing Question: “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n## Examples:\n\n\n\n# Example 1:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Fabian von Köppen - Geschäftsführer bei GARBE - \n- **Pain point:** Unstable Processes with Decentralized or Inadequate Data Management.\n- **Pain reliever:** Stabile Prozesse\n- **Pain Snippet:** durch stabile Prozesse und eine zentrale Datenbasis eine sichere Entscheidungsgrundlage besitzt und zusätzlich seinen Mitarbeitern ein effizienteres Arbeiten ermöglicht. \n\nInsbesondere ab Minute 00:25 wird auf diese und weitere Mehrwerte eingegangen. \n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, das zeigt wie Fabian von Köppen - Geschäftsführer bei GARBE - durch stabile Prozesse und eine zentrale Datenbasis eine sichere Entscheidungsgrundlage besitzt und zusätzlich seinen Mitarbeitern ein effizienteres Arbeiten ermöglicht. \n\nInsbesondere ab Minute 00:25 wird auf diese und weitere Mehrwerte eingegangen. \n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt?\n\n# Example 2:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Sven Seehawer (Geschäftsführer) und Robert Maaß (Teamleiter Projektcontrolling) von KVL \n- **Pain point:** \"Excel ist nicht nur langsam, sondern auch in Bezug auf die IT-Sicherheit fragwürdig und erzeugt Ängste\"\n- **Pain reliever:** Eigenständiger Zugriff auf individuell einstellbare Reporting-Ansicht basierend auf Echtzeit-Daten, kein Warten auf MA-Reportings\n- **Pain Snippet:** “das Warten auf MA-Reportings entfällt und ein neues Maß an Sicherheit und Kontrolle erreicht wird: \"Da habe ich klare Strukturen, es funktioniert immer gleich\".\n\nInsbesondere ab Minute 01:46 wird auf diese und weitere Mehrwerte eingegangen.\n\n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, das zeigt, wie Sven Seehawer (Geschäftsführer) und Robert Maaß (Teamleiter Projektcontrolling) von KVL durch den Einsatz einer Software mit klaren Strukturen, auf individuell einstellbare Reporting-Ansichten in Echtzeit zugreifen können, wodurch das Warten auf MA-Reportings entfällt und ein neues Maß an Sicherheit und Kontrolle erreicht wird: \"Da habe ich klare Strukturen, es funktioniert immer gleich\".\n\nInsbesondere ab Minute 01:46 wird auf diese und weitere Mehrwerte eingegangen.\n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt?\n\n# Example 3:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Torsten Hecht - Projektmanager bei der THOST Projektmanagement GmbH - \n- **Pain point:** Viel Kommunikation mit Projektbeteiligten via Meetings / Mails / Telefonate (Stress)\n- **Pain reliever:** Priorisierung von Aufgaben & Überblick über Fristen\n- **Pain Snippet:** \"riesigen E-Mail-Flut\", und \"irgendwelchen Telefonate\", überfordert war und den Überblick verlor. Durch den Einsatz von Alasco hat er nun eine verlässliche Echtzeit-Datengrundlage und zusätzlich eine Zeitersparnis von 75%  allein im Rechnungsprüfungslauf. \n\nInsbesondere ab Minute 01:30 wird auf diese und weitere Mehrwerte eingegangen.\n\n\n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, die beschreibt, wie Torsten Hecht - Projektmanager bei der THOST Projektmanagement GmbH - mit eine \"riesigen E-Mail-Flut\", und \"irgendwelchen Telefonate\", überfordert war und den Überblick verlor. Durch den Einsatz von Alasco hat er nun eine verlässliche Echtzeit-Datengrundlage und zusätzlich eine Zeitersparnis von 75%  allein im Rechnungsprüfungslauf. \n\nInsbesondere ab Minute 01:30 wird auf diese und weitere Mehrwerte eingegangen.\n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt? \n\n\n# Example 4:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Virom Subash - Head of Construction bei Kintyre - \n- **Pain point:** Mangelnder Überblick über Projektaufgaben sowie Fristen\n- **Pain reliever:** Minderung zeitintensiver Prozesse durch Workflows & automatisierte Datenübertragungen\n- **Pain Snippet:** und dank der Automatisierung, manuelle Aufgaben wie die Rechnungsabwicklung \"in einem ganz anderen Tempo\" erledigt.   \n\nInsbesondere ab Minute 01:25 wird auf diese und weitere Mehrwerte eingegangen. \n\n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** \nHier ein interessantes Video, das zeigt wie Virom Subash - Head of Construction bei Kintyre - immer den Überblick über den Projektstatus hat, und dank der Automatisierung, manuelle Aufgaben wie die Rechnungsabwicklung \"in einem ganz anderen Tempo\" erledigt.   \n\nInsbesondere ab Minute 01:25 wird auf diese und weitere Mehrwerte eingegangen. \n\nIst das ein Thema, das Sie aktuell ebenfalls beschäftigt? \n\n\n# Example 5:\n\n**Required Inputs:**\n- **Format:** Video\n- **Reference:** Gudrun Piesczeck - Projektleiterin bei der Rosa-Alscher-Gruppe - \n- **Pain point:** Schwierige Vorausplanung von anfallenden Kosten um Engpässe und Überfinanzierung zu vermeiden\n- **Pain reliever:** Besser Vorausplanen: Individuell einstellbare Mittelabflussplanung verknüpft mit dem Rechnungsprüflauf\n- **Pain Snippet:** \n- **Closing question:** “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n\n**Output:** Hier ein interessantes Video, das zeigt, wie Gudrun Piesczek - Projektleiterin bei der Rosa-Alscher Gruppe - eine strukturierte Software mit Rechnung-Workflow einsetzt um alle ihre Projektkosten besser zu planen und verwalten zu können.\n\nEin Thema, das auch Sie aktuell beschäftigt? \n Never ever use the word: 'aufschlussreiches'"
                },
                {
                "role": "user",
                "content": f"## **Your Turn**: Start writing your text below using the provided guidelines and framework. \n\n## Required Inputs:  \n\nFormat: Video\nReference: {reference} \nPain point: {painpoint} \nPain reliever: {value} \nPain Snippet: {painsnippet} \nClosing question: “Ist das ein Thema, das Sie aktuell ebenfalls beschäftigt?”\n"
                }
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response2 = response2.choices[0].message.content
        #st.write(response2)
        return response2
    
    except Exception as e:
        st.write(f"An error occurred: {e}")

if __name__ == "__main__":
    st.title("Alasco RRR Paragraph Writing Assistant")
    st.markdown("This tool helps you to write Alasco RRR paragraphs. Please select a maximum of 2 painpoints and 2 values.")


    #persona = st.radio("Persona", ["GF - Geschäftsführer", "PM - Projektleiter"])
    painpoint = st.multiselect("Painpoint", ["GF - Fehlende / veraltete Datengrundlage", "GF - Abhängigkeit von MAs", "PM - Mangelnder Überblick über Projektaufgaben sowie Fristen", "PM - Viel Kommunikation mit Projektbeteiligten via Meetings / Mails / Telefonate (Stress)", "PM -  Scattered management processes [logical]", "PM - Discontent with existing cost management solutions [logical]", "PM - Ineffective communication and information sharing [logical]"])
    value = st.multiselect("Value", ["GF - Multiprojektansicht, Transparenz in jedem Projekt", "GF - Eigenständiger Zugriff auf individuell einstellbare Reporting-Ansicht basierend auf Echtzeit-Daten, kein Warten auf MA-Reportings", "PM - Priorisierung von Aufgaben & Überblick über Fristen", "PM - Einfache Einbindung aller Projektbeteiligten inkl. Externer, Zusammenarbeit über Workflows", "PM - Centralized project management [logical]", "PM - Comprehensive and satisfying cost management solution [emotional/logical]", "PM - Streamlined communication with defined workflows [logical]"])
    
    #st.header("GF - Geschäftsführer", divider="rainbow")
    #st.subheader(":face_with_head_bandage: :red[Painpoints] ")
    
    #"GF - Fehlende / veraltete Datengrundlage", "GF - Abhängigkeit von MAs",
    
    #fehlende_veraltete_datengrundlage = st.checkbox('Fehlende / veraltete Datengrundlage')
    
    #if fehlende_veraltete_datengrundlage:
        #st.write('fehlende_veraltete_datengrundlage')


    #st.subheader(":sunglasses: :green[Value] ")



    if value == "GF - Multiprojektansicht, Transparenz in jedem Projekt":
        reference = "Philipp Pferschy (Geschäftsführer) und Ralf Ahles (Kaufmännischer Leiter) von GIEAG"
        painsnippet = "eine moderne Softwarelösung für das Multiprojektcontrolling einsetzt, die trotz hoher Anforderungen einen schnellen und zuverlässigen Überblick über alle Daten und Zahlen in Echtzeit bietet."
        source= "https://www.alasco.de/blog/goodbye-excel-akrobatik-so-geht-baucontrolling-heute/"
    elif value == "GF - Eigenständiger Zugriff auf individuell einstellbare Reporting-Ansicht basierend auf Echtzeit-Daten, kein Warten auf MA-Reportings":
        reference = "Sven Seehawer (Geschäftsführer) und Robert Maaß (Teamleiter Projektcontrolling) von KVL"
        painsnippet = "durch den Einsatz einer strukturierten Software, auf maßgeschneiderte Reports in Echtzeit zugreifen können. Dies spart nicht nur Zeit, indem das Warten auf Mitarbeiter-Reportings entfällt, sondern verstärkt auch die Entscheidungsautonomie und das Vertrauen der Stakeholder durch stets aktuelle Daten. Insbesondere ab Minute 01:46 wird auf diese und weitere Mehrwerte eingegangen."
        source= "https://www.alasco.de/referenzen/#kvl"
    elif value == "PM - Priorisierung von Aufgaben & Überblick über Fristen":
        reference = "Torsten Hecht - Projektmanager bei der THOST Projektmanagement GmbH - "
        painsnippet = "mit über 80 Rechnungen pro Tag zu kämpfen hatte und den Überblick verlor. Durch den Einsatz von Alasco hat er nun eine verlässliche Echtzeit-Datengrundlage und zusätzlich eine Zeitersparnis von 75%  allein im Rechnungsprüfungslauf. Insbesondere ab Minute 01:30 wird auf diese und weitere Mehrwerte eingegangen."
        source= "https://www.alasco.de/referenzen/#thost"
    elif value == "PM - Einfache Einbindung aller Projektbeteiligten inkl. Externer, Zusammenarbeit über Workflows":
        reference = "Ralf Ahles - kaufmännischer Leiter bei der GIEAG Immobilien AG -"
        painsnippet = "von Budgets, über Aufträge und Rechnungen bis hin zu Freigabeworkflows mit Projektaufgaben sowie Fristen alles zentral in einem System hat und dadurch auch die Zusammenarbeit mit Planern oder auch externen Nachunternehmern optimieren konnte. Insbesondere ab Minute 01:21 wird auf diese und weitere Mehrwerte eingegangen."
        source= "https://www.alasco.de/referenzen/#gieag"
    elif value == "PM - Centralized project management [logical]":
        reference = "Thimo Droste - Projektmanager bei der Augustus - "
        painsnippet = "'das mir in Zukunft und auch jetzt schon die Möglichkeit gibt neben all die Themen die ich bislang parallel und sehr ineffizienten fahren konnte, in diesem tool zu fahren und dadurch erstens viel Zeit zu sparen'"
        source= "https://www.alasco.de/referenzen/#augustus"
    elif value == "PM - Comprehensive and satisfying cost management solution [emotional/logical]":
        reference = "Thimo Droste - Projektmanager bei der Augustus - "
        painsnippet = "Alasco das erste Mal vorgestellt worden ist habe ich da eine sehr große Chance gesehen und ein sehr großes Entwicklungspotenzial und um Tool das mir in Zukunft und auch jetzt schon die Möglichkeit gibt'"
        source= "https://www.alasco.de/referenzen/#augustus"
    elif value == "PM - Streamlined communication with defined workflows [logical]":
        reference = "Thimo Droste - Projektmanager bei der Augustus - "
        painsnippet = "'Alasco eben einfach die Möglichkeit gibt in fest definierten Workflows Informationen transparent und eindeutig zu vermitteln.'"
        source= "https://www.alasco.de/referenzen/#augustus"

    else:
        reference = ""
        painsnippet = ""
        source= ""
    
    
    if st.button('Generate'):
        
        st.write("Generating Paragraphs...")
        col1, col2 = st.columns(2)
    
        with col1:
            st.write("**OPTION A**")
            response1 = paragraph_builder1(painpoint, reference, painsnippet, value, source)
            st.write(response1)
            st.markdown(f"**Source:** {source}")

        with col2:
            st.write("**OPTION B**",)
            response2 = paragraph_builder2(painpoint, reference, painsnippet, value, source)
            st.write(response2)
            st.markdown(f"**Source:** {source}")