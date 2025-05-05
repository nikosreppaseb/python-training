# UI Technical Design & Mockup Generation Prompt

## Context
I am developing an application called "Outsourcing App" and need to create UI Technical Design documentation including mockups. I have two markdown files containing the requirements:
1. Business Requirements document
2. Technical Requirements document containing NonFunctional Requirements, Functional Requirements, Functional Specifications, User Stories, and Acceptance Criteria

## Objective
Create a comprehensive UI Technical Design that includes:
- User interface mockups for all key screens/views
- Component hierarchy and relationships
- UI state management plan
- Navigation flow diagrams
- Design system specifications

## Input Files
I am providing two markdown files:
- [Business Requirements MD file]: Contains business goals, target users, and business processes
- [Technical Requirements MD file]: Contains detailed requirements including NFRs, functional requirements, specifications, user stories, and acceptance criteria

##StyleSheet example
For the style (css, colours, logos, etc) use the same like the www.nbg.gr website.

## Requirements for Output

### 1. UI Style Guide
- Define a consistent visual language (color palette, typography, spacing, etc.)
- Ensure compliance with any accessibility requirements specified in the NFRs
- Recommend UI component library options that align with technical constraints

### 2. Screen Mockups
- Create mockups for all primary user flows identified in the User Stories
- Include responsive design considerations for different device types
- Annotate each mockup with explanations of components and interactions

### 3. Component Architecture
- Break down UI into reusable components with clear responsibilities
- Define component props and state requirements
- Document component relationships and dependencies

### 4. Navigation & Flow
- Create user flow diagrams showing screen transitions
- Document navigation patterns and information architecture
- Map user stories to specific screens/flows

### 5. State Management
- Define UI state management approach
- Document data flow between API and UI components
- Identify client-side data storage needs

### 6. Interaction Design
- Define animations, transitions, and micro-interactions
- Document form validation rules and error handling
- Specify loading states and feedback mechanisms

### 7. Implementation Guidelines
- Provide technical recommendations for frontend implementation
- Address any technical constraints mentioned in the NFRs
- Include performance considerations for UI rendering

## Constraints & Special Considerations
- Please pay special attention to any compliance requirements mentioned in the NFRs
- If any requirements conflict, highlight these conflicts and suggest resolutions
- Consider any integration points with existing systems mentioned in the documents

## Output Format
Please provide:
1. A structured document with all the above sections
2. High-fidelity mockups for key screens
3. Component diagrams showing relationships
4. User flow diagrams
5. A summary section highlighting any key design decisions or assumptions made

