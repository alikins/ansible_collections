# Ansible module: ansible.module_office_365_connector_card


Use webhooks to create Connector Card messages within an Office 365 group

## Description

Creates Connector Card messages through
Office 365 Connectors U(https://dev.outlook.com/Connectors)

## Requirements

TODO

## Arguments

``` json
{
    "actions": "{'description': ['This array of objects will power the action links', 'found at the bottom of the card.']}",
    "color": "{'description': ['Accent color used for branding or indicating status in the card.']}",
    "sections": "{'description': ['Contains a list of sections to display in the card.', 'For more information see https://dev.outlook.com/Connectors/reference.']}",
    "summary": "{'description': ['A string used for summarizing card content.', 'This will be shown as the message subject.', "This is required if the text parameter isn't populated."]}",
    "text": "{'description': ['The main text of the card.', 'This will be rendered below the sender information and optional title,', 'and above any sections or actions present.']}",
    "title": "{'description': ['A title for the Connector message. Shown at the top of the message.']}",
    "webhook": "{'description': ['The webhook URL is given to you when you create a new Connector.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a simple Connector Card
  office_365_connector_card:
    webhook: https://outlook.office.com/webhook/GUID/IncomingWebhook/GUID/GUID
    text: 'Hello, World!'

- name: Create a Connector Card with the full format
  office_365_connector_card:
    webhook: https://outlook.office.com/webhook/GUID/IncomingWebhook/GUID/GUID
    summary: This is the summary property
    title: This is the **card's title** property
    text: This is the **card's text** property. Lorem ipsum dolor sit amet, consectetur
      adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    color: E81123
    sections:
    - title: This is the **section's title** property
      activity_image: http://connectorsdemo.azurewebsites.net/images/MSC12_Oscar_002.jpg
      activity_title: This is the section's **activityTitle** property
      activity_subtitle: This is the section's **activitySubtitle** property
      activity_text: This is the section's **activityText** property.
      hero_image:
        image: http://connectorsdemo.azurewebsites.net/images/WIN12_Scene_01.jpg
        title: This is the image's alternate text
      text: This is the section's text property. Lorem ipsum dolor sit amet, consectetur
        adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      facts:
      - name: This is a fact name
        value: This is a fact value
      - name: This is a fact name
        value: This is a fact value
      - name: This is a fact name
        value: This is a fact value
      images:
      - image: http://connectorsdemo.azurewebsites.net/images/MicrosoftSurface_024_Cafe_OH-06315_VS_R1c.jpg
        title: This is the image's alternate text
      - image: http://connectorsdemo.azurewebsites.net/images/WIN12_Scene_01.jpg
        title: This is the image's alternate text
      - image: http://connectorsdemo.azurewebsites.net/images/WIN12_Anthony_02.jpg
        title: This is the image's alternate text
      actions:
      - "@type": ActionCard
        name: Comment
        inputs:
        - "@type": TextInput
          id: comment
          is_multiline: true
          title: Input's title property
        actions:
        - "@type": HttpPOST
          name: Save
          target: http://...
      - "@type": ActionCard
        name: Due Date
        inputs:
        - "@type": DateInput
          id: dueDate
          title: Input's title property
        actions:
        - "@type": HttpPOST
          name: Save
          target: http://...
      - "@type": HttpPOST
        name: Action's name prop.
        target: http://...
      - "@type": OpenUri
        name: Action's name prop
        targets:
        - os: default
          uri: http://...
    - start_group: true
      title: This is the title of a **second section**
      text: This second section is visually separated from the first one by setting its
        **startGroup** property to true.

```

## License

TODO

## Author Information
  - ['Marc Sensenich']
